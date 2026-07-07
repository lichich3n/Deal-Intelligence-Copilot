import re

# =========================================================
# M&A TRANSACTION INTELLIGENCE ENGINE (PART 1)
# CORE EXTRACTION + CLEANING LAYER
# =========================================================

# =========================
# KEYWORDS
# =========================

KEYWORDS = {
    "Purchase Price": ["purchase price", "purchase consideration", "consideration"],
    "Enterprise Value": ["enterprise value", "transaction value"],
    "Offer Price": ["offer price", "per share"],
    "Premium": ["premium"],
}

# =========================
# TEXT UTILITIES
# =========================

def clean_text(text):
    return " ".join(text.split())


def find_context(text, keyword, window=250):
    lower = text.lower()
    pos = lower.find(keyword.lower())

    if pos == -1:
        return "Not detected"

    start = max(0, pos - window)
    end = min(len(text), pos + window)

    return text[start:end].replace("\n", " ")


def extract_between(text, keyword, chars=600):
    pos = text.lower().find(keyword.lower())
    if pos == -1:
        return "Not detected"

    snippet = text[pos:pos + chars]
    return " ".join(snippet.split())


# =========================
# VALUE EXTRACTION ENGINE
# =========================

def extract_value(text, keywords, pattern):
    lower = text.lower()

    for keyword in keywords:
        start = 0

        while True:
            pos = lower.find(keyword.lower(), start)
            if pos == -1:
                break

            snippet = text[pos:pos + 500]
            match = re.search(pattern, snippet, re.IGNORECASE)

            if match:
                return match.group(0)

            start = pos + 1

    return "Not detected"


# =========================
# NOISE FILTER SYSTEM
# =========================

def is_noise(text):
    noise = [
        "sale shares purchaser",
        "financial adviser",
        "independent board committee",
        "offeror",
        "scheme shareholders",
        "pursuant",
        "under chapter",
        "adviser"
    ]
    return any(n in text.lower() for n in noise)


# =========================
# BUYER / TARGET EXTRACTION
# =========================

def extract_buyer_target(text):
    text_clean = clean_text(text)

    buyer = "Not detected"
    target = "Not detected"

    # ---------------- BUYER ----------------
    m1 = re.search(
        r"acquisition by\s+(?:the\s+)?([A-Z][A-Za-z&\s\-]{2,120}?)\s+(?:of|for|under|pursuant)",
        text_clean,
        re.IGNORECASE
    )

    if m1:
        candidate = m1.group(1).strip()
        if not is_noise(candidate):
            buyer = candidate

    # ---------------- TARGET ----------------
    m2 = re.search(
        r"acquisition of\s+(?:[\d,\.]+\s+)?([A-Z][A-Za-z&\-\s]{2,120}?)(?:\s+(?:Shares|share|under|pursuant|in))",
        text_clean,
        re.IGNORECASE
    )

    if m2:
        candidate = m2.group(1).strip()
        candidate = re.sub(r"\b(Shares|Share|Sale|Purchaser)\b", "", candidate)
        candidate = re.sub(r"\s{2,}", " ", candidate).strip()

        if not is_noise(candidate) and not re.search(r"\d", candidate):
            target = candidate

    return buyer, target


# =========================
# CONSIDERATION ENGINE
# =========================

def detect_consideration(text):
    lower = text.lower()

    cash = any(x in lower for x in [
        "cash consideration",
        "cash offer",
        "cash"
    ])

    stock = any(x in lower for x in [
        "share consideration",
        "share exchange",
        "stock consideration",
        "share offer"
    ])

    if cash and stock:
        return "Mixed"
    elif cash:
        return "Cash"
    elif stock:
        return "Stock"
    else:
        return "Not detected"


# =========================
# SECTION EXTRACTION ENGINE
# =========================

def extract_section(text, heading):
    pattern = rf"{heading}.*?(?=\n[A-Z][A-Za-z &()\-]{{2,}}|\Z)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return " ".join(match.group(0).split())

    idx = text.lower().find(heading.lower())
    if idx == -1:
        return "Not detected"

    return " ".join(text[idx:idx + 600].split())

# =========================================================
# M&A TRANSACTION INTELLIGENCE ENGINE (PART 2)
# ANALYSIS + REPORT GENERATION LAYER
# =========================================================

# =========================
# MAIN ANALYZER
# =========================

def analyze_transaction(text):

    report = {}
    lower = text.lower()

    # ---------------- TYPE CLASSIFICATION ----------------
    if "merger" in lower:
        report["Transaction Type"] = "Merger"
    elif "acquisition" in lower:
        report["Transaction Type"] = "Acquisition"
    elif "takeover" in lower:
        report["Transaction Type"] = "Takeover"
    else:
        report["Transaction Type"] = "Unknown"

    # ---------------- BUYER / TARGET ----------------
    buyer, target = extract_buyer_target(text)
    report["Buyer"] = buyer
    report["Target"] = target

    # ---------------- CONSIDERATION ----------------
    report["Consideration"] = detect_consideration(text)

    # ---------------- FINANCIAL FIGURES ----------------
    money = re.findall(
        r"(?:HK\$|US\$|GBP|EUR|RMB|C\$|¥|\$)\s?[\d,.]+(?:\s*(?:million|billion|bn|m))?",
        text,
        re.IGNORECASE
    )

    percent = re.findall(r"\d+(?:\.\d+)?%", text)

    report["Money Figures"] = list(dict.fromkeys(money))[:20]
    report["Percentages"] = list(dict.fromkeys(percent))[:20]

    # ---------------- VALUATION METRICS ----------------
    report["Purchase Price"] = extract_value(
        text,
        KEYWORDS["Purchase Price"],
        r"(?:HK\$|US\$|GBP|EUR|C\$)\s?[\d,.]+(?:\s*(?:million|billion|bn|m))?"
    )

    report["Enterprise Value"] = extract_value(
        text,
        KEYWORDS["Enterprise Value"],
        r"(?:HK\$|US\$|GBP|EUR|C\$)\s?[\d,.]+(?:\s*(?:million|billion|bn|m))?"
    )

    report["Offer Price"] = extract_value(
        text,
        KEYWORDS["Offer Price"],
        r"(?:HK\$|US\$|GBP|EUR|C\$)\s?[\d,.]+(?:\s*(?:per share|/share))?"
    )

    report["Premium"] = extract_value(
        text,
        KEYWORDS["Premium"],
        r"\d+(?:\.\d+)?%"
    )

    # ---------------- QUALITATIVE ANALYSIS ----------------
    report["Strategic Rationale"] = extract_section(text, "Strategic Rationale")
    report["Regulatory Approvals"] = extract_section(text, "Regulatory Approvals")
    report["Risks"] = extract_section(text, "Risks")

    # ---------------- DEAL SCORE ----------------
    score = 0

    score_map = {
        "Purchase Price": 25,
        "Enterprise Value": 25,
        "Offer Price": 20,
        "Premium": 15,
        "Buyer": 5,
        "Target": 5,
        "Consideration": 5
    }

    for k, v in score_map.items():
        if report.get(k) != "Not detected":
            score += v

    report["Deal Score"] = f"{min(score, 100)}/100"

    # ---------------- DEAL SUMMARY ----------------
    report["Deal Summary"] = {
        "Buyer": report["Buyer"],
        "Target": report["Target"],
        "Transaction Type": report["Transaction Type"],
        "Consideration": report["Consideration"],
        "Purchase Price": report["Purchase Price"],
        "Enterprise Value": report["Enterprise Value"],
        "Offer Price": report["Offer Price"],
        "Premium": report["Premium"]
    }

    return report


# =========================
# OPTIONAL DEBUG HELPERS
# =========================

def debug_keys(report):
    return {k: type(v) for k, v in report.items()}


def validate_report(report):
    required = [
        "Buyer",
        "Target",
        "Transaction Type",
        "Deal Summary"
    ]

    return all(k in report for k in required)
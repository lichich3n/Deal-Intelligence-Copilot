import re

def create_briefing(text):

    briefing = {}

    # First 3 paragraphs usually explain the transaction
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 80]

    briefing["Executive Summary"] = "\n\n".join(paragraphs[:3])

    keywords = {
        "Cash": len(re.findall(r"\bcash\b", text, re.IGNORECASE)),
        "Debt": len(re.findall(r"\bdebt\b", text, re.IGNORECASE)),
        "Loan": len(re.findall(r"\bloan\b", text, re.IGNORECASE)),
        "Equity": len(re.findall(r"\bequity\b", text, re.IGNORECASE)),
        "Share": len(re.findall(r"\bshare", text, re.IGNORECASE)),
        "Merger": len(re.findall(r"\bmerger\b", text, re.IGNORECASE)),
        "Acquisition": len(re.findall(r"\bacquisition\b", text, re.IGNORECASE)),
        "Synergy": len(re.findall(r"\bsynerg", text, re.IGNORECASE))
    }

    briefing["Keyword Counts"] = keywords

    return briefing
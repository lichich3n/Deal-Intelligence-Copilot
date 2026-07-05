import re

def analyze_transaction(text):

    report = {}

    report["Document Length"] = len(text)

    money = re.findall(r"(HK\$|US\$|RMB|¥|\$)\s?[\d,]+(?:\.\d+)?\s?(?:billion|million|bn|m)?", text, re.IGNORECASE)

    percentages = re.findall(r"\d+(?:\.\d+)?%", text)

    report["Money Figures"] = list(set(money[:15]))

    report["Percentages"] = list(set(percentages[:15]))

    return report
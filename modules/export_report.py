def print_report(report):

    print("\n" + "=" * 70)
    print("              M&A TRANSACTION INTELLIGENCE")
    print("=" * 70)

    # =====================================================
    # DEAL SUMMARY
    # =====================================================

    summary = report.get("Deal Summary", {})

    print("\nDEAL SUMMARY")
    print("-" * 70)

    print(f"Buyer            : {report.get('Buyer', 'Not detected')}")
    print(f"Target           : {report.get('Target', 'Not detected')}")
    print(f"Transaction Type : {summary.get('Transaction Type', 'Not detected')}")
    print(f"Consideration    : {summary.get('Consideration', 'Not detected')}")
    print(f"Purchase Price   : {summary.get('Purchase Price', 'Not detected')}")
    print(f"Enterprise Value : {summary.get('Enterprise Value', 'Not detected')}")
    print(f"Premium          : {summary.get('Premium', 'Not detected')}")

    print("\nOverview")
    print(summary.get("Overview", "Not detected"))

    # =====================================================
    # TRANSACTION DETAILS
    # =====================================================

    print("\n" + "-" * 70)
    print("TRANSACTION DETAILS")
    print("-" * 70)

    details = [
        "Transaction Type",
        "Consideration",
        "Purchase Price",
        "Enterprise Value",
        "Offer Price",
        "Premium"
    ]

    for item in details:

        print(f"\n{item}")
        print(report.get(item, "Not detected"))

    # =====================================================
    # STRATEGIC ANALYSIS
    # =====================================================

    print("\n" + "-" * 70)
    print("STRATEGIC ANALYSIS")
    print("-" * 70)

    strategy = [
        "Strategic Rationale",
        "Regulatory Approvals",
        "Risks"
    ]

    for item in strategy:

        print(f"\n{item}")
        print(report.get(item, "Not detected"))

    # =====================================================
    # KEY FINANCIAL FIGURES
    # =====================================================

    print("\n" + "-" * 70)
    print("KEY FINANCIAL FIGURES")
    print("-" * 70)

    print("\nMoney Figures")

    for value in report.get("Money Figures", []):
        print("•", value)

    print("\nPercentages")

    for value in report.get("Percentages", []):
        print("•", value)

    print("\nDeal Score")
    print(report.get("Deal Score", "N/A"))

    print("\n" + "=" * 70)


def export_report(report, briefing, questions, tasks):

    import os

    os.makedirs("outputs", exist_ok=True)

    filename = os.path.join(
        "outputs",
        "Deal_Intelligence_Report.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("M&A TRANSACTION INTELLIGENCE REPORT\n")
        file.write("=" * 70 + "\n\n")

        # =====================================================
        # DEAL SUMMARY
        # =====================================================

        summary = report.get("Deal Summary", {})

        file.write("DEAL SUMMARY\n")
        file.write("-" * 70 + "\n\n")

        file.write(f"Buyer              : {report.get('Buyer', 'Not detected')}\n")
        file.write(f"Target             : {report.get('Target', 'Not detected')}\n")
        file.write(f"Transaction Type   : {summary.get('Transaction Type', 'Not detected')}\n")
        file.write(f"Consideration      : {summary.get('Consideration', 'Not detected')}\n")
        file.write(f"Purchase Price     : {summary.get('Purchase Price', 'Not detected')}\n")
        file.write(f"Enterprise Value   : {summary.get('Enterprise Value', 'Not detected')}\n")
        file.write(f"Premium            : {summary.get('Premium', 'Not detected')}\n")
        file.write(f"Deal Score         : {report.get('Deal Score', 'N/A')}\n\n")

        file.write("Overview\n")
        file.write(summary.get("Overview", "Not detected"))
        file.write("\n\n")

        # =====================================================
        # TRANSACTION DETAILS
        # =====================================================

        file.write("=" * 70 + "\n")
        file.write("TRANSACTION DETAILS\n")
        file.write("=" * 70 + "\n\n")

        for item in [
            "Transaction Type",
            "Consideration",
            "Purchase Price",
            "Enterprise Value",
            "Offer Price",
            "Premium"
        ]:
            file.write(item + "\n")
            file.write(str(report.get(item, "Not detected")))
            file.write("\n\n")

        # =====================================================
        # STRATEGIC ANALYSIS
        # =====================================================

        file.write("=" * 70 + "\n")
        file.write("STRATEGIC ANALYSIS\n")
        file.write("=" * 70 + "\n\n")

        for item in [
            "Strategic Rationale",
            "Regulatory Approvals",
            "Risks"
        ]:
            file.write(item + "\n")
            file.write(str(report.get(item, "Not detected")))
            file.write("\n\n")

        # =====================================================
        # KEY FINANCIAL FIGURES
        # =====================================================

        file.write("=" * 70 + "\n")
        file.write("KEY FINANCIAL FIGURES\n")
        file.write("=" * 70 + "\n\n")

        file.write("Money Figures\n")

        for value in report.get("Money Figures", []):
            file.write(f"• {value}\n")

        file.write("\nPercentages\n")

        for value in report.get("Percentages", []):
            file.write(f"• {value}\n")

        # =====================================================
        # ANALYST BRIEFING
        # =====================================================

        file.write("\n\n")
        file.write("=" * 70 + "\n")
        file.write("ANALYST BRIEFING\n")
        file.write("=" * 70 + "\n\n")

        for key, value in briefing.items():
            file.write(key + "\n")
            file.write(str(value))
            file.write("\n\n")

        # =====================================================
        # CHALLENGE MODE
        # =====================================================

        file.write("=" * 70 + "\n")
        file.write("ASSOCIATE CHALLENGE MODE\n")
        file.write("=" * 70 + "\n\n")

        for i, question in enumerate(questions, 1):
            file.write(f"{i}. {question}\n")

        # =====================================================
        # NEXT STEPS
        # =====================================================

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write("RECOMMENDED NEXT STEPS\n")
        file.write("=" * 70 + "\n\n")

        for i, task in enumerate(tasks, 1):
            file.write(f"{i}. {task}\n")

    return filename
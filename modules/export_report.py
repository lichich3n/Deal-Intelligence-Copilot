from pathlib import Path

def export_report(report, briefing, questions, tasks):

    output_folder = Path("outputs")
    output_folder.mkdir(exist_ok=True)

    file = output_folder / "Deal_Report.txt"

    with open(file, "w", encoding="utf-8") as f:

        f.write("="*70 + "\n")
        f.write("DEAL INTELLIGENCE REPORT\n")
        f.write("="*70 + "\n\n")

        for key, value in report.items():
            f.write(f"{key}\n")
            f.write(str(value))
            f.write("\n\n")

        f.write("="*70 + "\n")
        f.write("ANALYST BRIEFING\n")
        f.write("="*70 + "\n\n")

        for key, value in briefing.items():
            f.write(f"{key}\n")
            f.write(str(value))
            f.write("\n\n")

        f.write("="*70 + "\n")
        f.write("ASSOCIATE CHALLENGE MODE\n")
        f.write("="*70 + "\n\n")

        for question in questions:
            f.write("- " + question + "\n")

        f.write("\n")

        f.write("="*70 + "\n")
        f.write("RECOMMENDED NEXT STEPS\n")
        f.write("="*70 + "\n\n")

        for task in tasks:
            f.write("- " + task + "\n")

    return file
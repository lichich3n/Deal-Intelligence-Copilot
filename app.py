from modules.export_report import export_report
from modules.next_steps import recommend_next_steps
from modules.challenge_mode import generate_challenges
from modules.briefing import create_briefing
from modules.transaction_analyzer import analyze_transaction
from modules.pdf_reader import extract_text
from pathlib import Path

print("=" * 60)
print("        ANALYST COPILOT")
print("=" * 60)

print("\nSupported Documents:")
print("1. HKEX Announcement")
print("2. Press Release")
print("3. Annual Report (Coming Soon)")
print("4. Investor Presentation (Coming Soon)")

choice = input("\nSelect document type (1-4): ")

documents_folder = Path("sample_documents")

pdf_files = list(documents_folder.glob("*.pdf"))

if len(pdf_files) == 0:
    print("\nNo PDF files found.")
    print("Place a PDF inside the sample_documents folder.")
    exit()

print("\nAvailable Documents:")

for i, pdf in enumerate(pdf_files):
    print(f"{i+1}. {pdf.name}")

selection = int(input("\nChoose a file: "))

selected_file = pdf_files[selection-1]

print("\nSelected:")
print(selected_file.name)
print("\nReading document...\n")

text = extract_text(selected_file)

report = analyze_transaction(text)
briefing = create_briefing(text)
questions = generate_challenges(text)
tasks = recommend_next_steps(text)

print("\n==============================")
print("DEAL INTELLIGENCE REPORT")
print("==============================")

for key, value in report.items():
    print(f"\n{key}:")
    print(value)

    print("\n")
print("="*60)
print("ANALYST BRIEFING")
print("="*60)

for key, value in briefing.items():
    print(f"\n{key}")
    print(value)

    print("\n")
print("=" * 60)
print("ASSOCIATE CHALLENGE MODE")
print("=" * 60)

for i, question in enumerate(questions, 1):
    print(f"{i}. {question}")

    print("\n")
print("=" * 60)
print("RECOMMENDED ANALYST NEXT STEPS")
print("=" * 60)

for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

    output = export_report(report, briefing, questions, tasks)

print("\n")
print("="*60)
print("REPORT SAVED")
print("="*60)
print(output)
# 📊 Deal Intelligence Copilot

An AI-assisted workflow tool designed to accelerate the first-pass analysis of public M&A transaction documents.

The application extracts key transaction information from HKEX announcements and merger documents, automatically generating analyst-style summaries, Investment Committee (IC) briefing materials, transaction highlights and discussion points.

The project was built to explore how AI can improve analyst productivity by reducing manual document review while leaving investment judgement to professionals.

---

# Why I Built This

Investment professionals regularly review hundreds of pages of transaction announcements, circulars and regulatory filings before beginning analysis.

This project explores how AI can automate repetitive information extraction and document summarisation so analysts can spend more time on valuation, strategic thinking and investment decisions.

Rather than replacing analyst judgement, the goal is to improve workflow efficiency.

---

# Key Features

✅ PDF transaction document upload

✅ Automatic transaction classification

✅ Buyer and target extraction

✅ Purchase price extraction

✅ Enterprise value extraction

✅ Offer price detection

✅ Premium extraction

✅ Consideration type detection

✅ Financial figure extraction

✅ Strategic rationale extraction

✅ Regulatory approval extraction

✅ Risk factor identification

✅ Investment Committee (IC) memo generation

✅ Executive briefing generation

✅ Analyst challenge questions

✅ Recommended next steps

✅ Streamlit dashboard interface

---

# Example Workflow

```
HKEX Announcement PDF
            │
            ▼
      PDF Text Extraction
            │
            ▼
 Transaction Intelligence Engine
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼
Financial Strategic  Risk
Extraction Analysis Assessment
            │
            ▼
Investment Committee Memo
            │
            ▼
 Analyst Dashboard
```

---

# Example Output

The system produces an analyst-style report including:

- Deal Summary
- Buyer & Target
- Transaction Type
- Purchase Price
- Enterprise Value
- Premium
- Consideration
- Executive Summary
- Strategic Rationale
- Regulatory Considerations
- Risk Assessment
- Analyst Challenge Questions
- Recommended Next Steps

---

# Technology Stack

- Python
- Streamlit
- Regular Expressions (Regex)
- PDF Parsing
- Natural Language Processing (rule-based)
- Git
- GitHub

---

# Repository Structure

```
Deal-Intelligence-Copilot/
│
├── app.py
├── cli_app.py
├── modules/
│   ├── transaction_analyzer.py
│   ├── pdf_reader.py
│   ├── briefing.py
│   ├── challenge_mode.py
│   ├── next_steps.py
│   └── export_report.py
│
├── sample_documents/
├── screenshots/
└── README.md
```

---

# Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the Streamlit application

```bash
python -m streamlit run app.py
```

Upload a supported M&A PDF document and generate the Deal Intelligence report.

---

# Future Improvements

- GPT-powered transaction understanding
- Named Entity Recognition (NER)
- Multiple jurisdiction support
- SEC EDGAR integration
- Bloomberg and Refinitiv data integration
- Financial ratio extraction
- Comparable transaction database
- AI-generated valuation commentary
- Multi-document transaction comparison

---

# Disclaimer

This project is intended for educational and research purposes.

It analyses publicly available transaction documents and should not be interpreted as investment advice or a substitute for professional financial analysis.

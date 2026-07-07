import streamlit as st
import tempfile

from modules.pdf_reader import extract_text
from modules.transaction_analyzer import analyze_transaction

# -------------------------
# PAGE CONFIG (BLOOMBERG STYLE)
# -------------------------
st.set_page_config(
    page_title="Deal Intelligence Copilot",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# DARK BLOOMBERG STYLE CSS
# -------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f14;
        color: #ffffff;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    h1, h2, h3 {
        color: #00ff9d;
        font-family: monospace;
    }

    .metric-box {
        background-color: #111827;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1f2937;
    }

    .section-title {
        color: #00ff9d;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        font-family: monospace;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# HEADER
# -------------------------
st.title("📊 DEAL INTELLIGENCE COPILOT")
st.caption("Deal intelligence system powered by NLP extraction by LC")

st.divider()

# -------------------------
# UPLOAD SECTION
# -------------------------
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Upload M&A / HKEX PDF", type=["pdf"])

with col2:
    st.info("Supported: HKEX announcements, M&A circulars")

st.divider()

# -------------------------
# MAIN LOGIC
# -------------------------
if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    text = extract_text(tmp_path)

if st.button("Generate Analysis"):

    if not text.strip():
        st.error("Please provide transaction text")
        st.stop()

    with st.spinner("Building Investment Committee Memo..."):

        report = analyze_transaction(text)

        from modules.briefing import create_briefing
        from modules.challenge_mode import generate_challenges
        from modules.next_steps import recommend_next_steps

        briefing = create_briefing(text)
        challenges = generate_challenges(text)
        next_steps = recommend_next_steps(text)

    # =========================
    # IC DECISION ENGINE (SIMPLE LOGIC LAYER)
    # =========================

    score = report.get("Deal Score", "0/100")
    try:
        numeric_score = int(str(score).split("/")[0])
    except:
        numeric_score = 0

    if numeric_score >= 80:
        recommendation = "🟢 APPROVE"
    elif numeric_score >= 60:
        recommendation = "🟡 REVIEW"
    else:
        recommendation = "🔴 REJECT / HIGH RISK"

    # =========================
    # IC MEMO TABS (BANK STYLE)
    # =========================

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📄 Summary",
        "💰 Valuation & Terms",
        "🧠 Strategic Rationale",
        "⚠️ Risks & Regulatory",
        "⚔️ Challenge Questions",
        "📌 Recommendation"
    ])

    # =========================
    # TAB 1 — IC SUMMARY
    # =========================
    with tab1:

        st.markdown("## Investment Committee Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric("Buyer", report.get("Buyer"))
        col2.metric("Target", report.get("Target"))
        col3.metric("Deal Type", report.get("Transaction Type"))

        st.divider()

        st.markdown("### Overview")

        st.write(f"""
        This Investment Committee memo summarises the proposed transaction involving **{report.get('Buyer')} acquiring {report.get('Target')}**.

        The deal is classified as a **{report.get('Transaction Type')}** transaction with a preliminary score of **{score}**.
        """)

    # =========================
    # TAB 2 — VALUATION & TERMS
    # =========================
    with tab2:

        st.markdown("## Valuation & Deal Terms")

        c1, c2, c3 = st.columns(3)

        c1.metric("Purchase Price", report.get("Purchase Price"))
        c2.metric("Enterprise Value", report.get("Enterprise Value"))
        c3.metric("Premium", report.get("Premium"))

        st.divider()

        st.markdown("### Additional Financial Data")
        st.write(report.get("Money Figures"))
        st.write(report.get("Percentages"))

    # =========================
    # TAB 3 — STRATEGIC RATIONALE
    # =========================
    with tab3:

        st.markdown("## Strategic Rationale")

        st.write(report.get("Strategic Rationale"))

        st.divider()

        st.markdown("### Analyst Briefing")

        st.write(briefing)

    # =========================
    # TAB 4 — RISKS
    # =========================
    with tab4:

        st.markdown("## Risk & Regulatory Assessment")

        st.subheader("Regulatory Considerations")
        st.write(report.get("Regulatory Approvals"))

        st.subheader("Risk Factors")
        st.write(report.get("Risks"))

    # =========================
    # TAB 5 — CHALLENGE MODE
    # =========================
    with tab5:

        st.markdown("## Challenge Questions")

        for i, q in enumerate(challenges, 1):
            st.write(f"**{i}.** {q}")

    # =========================
    # TAB 6 — RECOMMENDATION ENGINE
    # =========================
    with tab6:

        st.markdown("## Investment Committee Recommendation")

        st.subheader("Final Decision")

        st.markdown(f"### {recommendation}")

        st.divider()

        st.markdown("## Execution Roadmap")

        for i, step in enumerate(next_steps, 1):
            st.write(f"{i}. {step}")

        st.divider()

        st.success("ANALYSIS GENERATED SUCCESSFULLY")

else:
    st.warning("Upload a PDF to begin analysis")
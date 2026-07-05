def generate_challenges(text):

    text = text.lower()

    questions = []

    if "cash" in text:
        questions.append(
            "Transaction appears to include cash consideration. Analyse post-deal leverage and financing capacity."
        )

    if "share" in text or "stock" in text:
        questions.append(
            "Transaction includes equity consideration. Assess shareholder dilution and EPS impact."
        )

    if "synerg" in text:
        questions.append(
            "Management mentions synergies. Are these quantified, realistic and supported by comparable transactions?"
        )

    if "premium" in text:
        questions.append(
            "Compare the acquisition premium against recent precedent transactions in the same sector."
        )

    if "regulatory" in text or "approval" in text:
        questions.append(
            "Identify regulatory approvals that could delay or block completion of the transaction."
        )

    if "goodwill" not in text:
        questions.append(
            "Estimate goodwill creation and determine whether a Purchase Price Allocation (PPA) should be modelled."
        )

    questions.append(
        "Would a private equity buyer value this transaction differently from a strategic acquirer?"
    )

    questions.append(
        "What information is still missing before building a merger model?"
    )

    return questions
def recommend_next_steps(text):

    text = text.lower()

    tasks = []

    # Core tasks every analyst should consider
    tasks.append("Review transaction structure")
    tasks.append("Identify comparable companies")
    tasks.append("Review recent precedent transactions")

    if "cash" in text:
        tasks.append("Model post-acquisition leverage")

    if "share" in text or "stock" in text:
        tasks.append("Build accretion/dilution model")

    if "goodwill" in text or "purchase price" in text:
        tasks.append("Estimate Purchase Price Allocation (PPA)")

    if "synerg" in text:
        tasks.append("Validate management synergy assumptions")

    if "approval" in text or "regulatory" in text:
        tasks.append("Assess regulatory approval timeline")

    tasks.append("Prepare analyst discussion points for Associate")

    return tasks
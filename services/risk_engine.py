def calculate_risk(metrics):
    """
    Simulates an AI-based data quality assessment.
    """

    completeness = metrics["completeness_score"]
    consistency = metrics["consistency_score"]

    quality_score = round(
        (completeness * 0.6) +
        (consistency * 0.4),
        2
    )

    anomaly_probability = round(100 - quality_score, 2)

    if quality_score >= 90:
        risk = "Low"

    elif quality_score >= 70:
        risk = "Medium"

    else:
        risk = "High"

    return {
        "quality_score": quality_score,
        "anomaly_probability": anomaly_probability,
        "risk": risk
    }
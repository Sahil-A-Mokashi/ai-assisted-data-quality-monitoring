from flask import Blueprint, jsonify
from models import Dataset, QualityMetrics

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/reports/<int:dataset_id>", methods=["GET"])
def get_dataset_report(dataset_id):

    dataset = Dataset.query.get(dataset_id)

    if dataset is None:
        return jsonify({"error": "Dataset not found"}), 404

    metrics = QualityMetrics.query.filter_by(
        dataset_id=dataset_id
    ).first()

    return jsonify({
        "dataset": dataset.to_dict(),
        "metrics": metrics.to_dict() if metrics else None
    })

@reports_bp.route("/dashboard", methods=["GET"])
def dashboard():

    datasets = Dataset.query.all()

    total = len(datasets)

    low = sum(
        1 for d in datasets
        if d.predicted_risk == "Low"
    )

    medium = sum(
        1 for d in datasets
        if d.predicted_risk == "Medium"
    )

    high = sum(
        1 for d in datasets
        if d.predicted_risk == "High"
    )

    avg_quality = round(
        sum(d.quality_score for d in datasets) / total,
        2
    ) if total else 0

    return jsonify({
        "total_datasets": total,
        "low_risk": low,
        "medium_risk": medium,
        "high_risk": high,
        "average_quality_score": avg_quality
    })
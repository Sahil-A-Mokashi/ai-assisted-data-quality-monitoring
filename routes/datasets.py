from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import tempfile
import os
from database import db
from sqlalchemy import or_
from models import Dataset, QualityMetrics
from services.profiler import profile_csv
from services.risk_engine import calculate_risk


ALLOWED_EXTENSIONS = {"csv"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

datasets_bp = Blueprint("datasets", __name__)


@datasets_bp.route("/datasets", methods=["GET"])
def get_datasets():

    query = Dataset.query

    # ----------------------------
    # Search across text fields
    # ----------------------------

    search = request.args.get("search")

    if search:
        query = query.filter(
            or_(
                Dataset.dataset_name.ilike(f"%{search}%"),
                Dataset.organisation.ilike(f"%{search}%"),
                Dataset.source_system.ilike(f"%{search}%"),
                Dataset.domain.ilike(f"%{search}%"),
                Dataset.uploaded_by.ilike(f"%{search}%"),
                Dataset.notes.ilike(f"%{search}%")
            )
        )

    # ----------------------------
    # Dynamic Filters
    # ----------------------------

    filterable_fields = [
        "dataset_id",
        "dataset_name",
        "organisation",
        "source_system",
        "domain",
        "uploaded_by",
        "status",
        "predicted_risk",
        "quality_score",
        "total_rows",
        "total_columns",
        "upload_date",
        "file_name"
    ]

    for field in filterable_fields:

        value = request.args.get(field)

        if value is not None:

            column = getattr(Dataset, field)

            query = query.filter(column == value)

    # ----------------------------
    # Sorting
    # ----------------------------

    sort = request.args.get("sort")

    order = request.args.get("order", "asc")

    if sort:

        if hasattr(Dataset, sort):

            column = getattr(Dataset, sort)

            if order.lower() == "desc":
                query = query.order_by(column.desc())
            else:
                query = query.order_by(column.asc())

    datasets = query.all()

    return jsonify([dataset.to_dict() for dataset in datasets])

@datasets_bp.route("/datasets", methods=["POST"])
def create_dataset():

    dataset_name = request.form.get("dataset_name", "").strip()
    organisation = request.form.get("organisation", "").strip()

    if not dataset_name:
        return jsonify({"error": "Dataset name is required."}), 400

    if not organisation:
        return jsonify({"error": "Organisation is required."}), 400

    if "file" not in request.files:
        return jsonify({"error": "CSV file is required."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Only CSV files are allowed."}), 400

    filename = secure_filename(file.filename)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        file.save(temp_file.name)
        temp_path = temp_file.name

    metrics = profile_csv(temp_path)
    risk = calculate_risk(metrics)

    dataset = Dataset(
        dataset_name=dataset_name,
        organisation=organisation,
        source_system=request.form.get("source_system", ""),
        domain=request.form.get("domain", ""),
        uploaded_by=request.form.get("uploaded_by", ""),
        notes=request.form.get("notes", ""),
        file_name=filename,
        quality_score=risk["quality_score"],
        predicted_risk=risk["risk"],
        total_rows=metrics["total_rows"],
        total_columns=metrics["total_columns"]
    )

    db.session.add(dataset)
    db.session.commit()

    metrics_record = QualityMetrics(
        dataset_id=dataset.dataset_id,
        missing_values=metrics["missing_values"],
        duplicate_rows=metrics["duplicate_rows"],
        null_percentage=metrics["null_percentage"],
        completeness_score=metrics["completeness_score"],
        consistency_score=metrics["consistency_score"],
        anomaly_probability = risk["anomaly_probability"],
        anomaly_status = risk["risk"]
    )

    db.session.add(metrics_record)
    db.session.commit()

    os.remove(temp_path)

    return jsonify(dataset.to_dict()), 201
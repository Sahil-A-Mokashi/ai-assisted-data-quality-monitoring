from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import tempfile
import os
from database import db
from models import Dataset


ALLOWED_EXTENSIONS = {"csv"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

datasets_bp = Blueprint("datasets", __name__)


@datasets_bp.route("/datasets", methods=["GET"])
def get_datasets():
    datasets = Dataset.query.all()

    return jsonify([
        dataset.to_dict()
        for dataset in datasets
    ])

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

    dataset = Dataset(
        dataset_name=dataset_name,
        organisation=organisation,
        source_system=request.form.get("source_system", ""),
        domain=request.form.get("domain", ""),
        uploaded_by=request.form.get("uploaded_by", ""),
        notes=request.form.get("notes", ""),
        file_name=filename
    )

    db.session.add(dataset)
    db.session.commit()

    os.remove(temp_path)

    return jsonify(dataset.to_dict()), 201
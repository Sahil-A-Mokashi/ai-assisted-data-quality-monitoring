from flask import Blueprint, jsonify
from models import Dataset

datasets_bp = Blueprint("datasets", __name__)


@datasets_bp.route("/datasets", methods=["GET"])
def get_datasets():
    datasets = Dataset.query.all()

    return jsonify([
        dataset.to_dict()
        for dataset in datasets
    ])
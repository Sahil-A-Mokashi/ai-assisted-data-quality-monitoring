from flask import Blueprint, jsonify

datasets_bp = Blueprint("datasets", __name__)


@datasets_bp.route("/datasets", methods=["GET"])
def get_datasets():
    return jsonify([])
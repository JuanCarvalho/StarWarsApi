from flask import Blueprint, jsonify

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.factories import api_rest_factory

health_bp = Blueprint("health", __name__)

api_rest_adapter: ApiRestContract = api_rest_factory.create("flaskapi_adapter")


@health_bp.route("/health", methods=["GET"])
def health_check():
    response = api_rest_adapter.health_check()
    return jsonify(response)

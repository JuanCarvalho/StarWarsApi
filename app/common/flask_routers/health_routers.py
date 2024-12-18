from flask import jsonify
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.factories import api_rest_factory

health_ns = Namespace("health", description="Health Check operations")


@health_ns.route("/")
class HealthCheckResource(Resource):
    def get(self):
        """
        Health check endpoint
        """
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter")
        response = api_rest_adapter.health_check()
        return jsonify(response)

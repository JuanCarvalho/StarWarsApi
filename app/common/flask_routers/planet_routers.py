from flask import jsonify
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.factories import api_rest_factory

planets_ns = Namespace("planet", description="Planets operations")


@planets_ns.route("/")
class PlanetsResourceList(Resource):
    @planets_ns.doc(description="List all planets", responses={200: "Success"})
    def get(self):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        response = api_rest_adapter.list()
        return jsonify([response, response])


@planets_ns.route("/<string:id>")
class PlanetsResourceGet(Resource):
    @planets_ns.doc(description="Get planet by id", responses={200: "Success", 404: "Planet not found"})
    def get(self, id: str):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        response = api_rest_adapter.get(id)
        return jsonify(response)

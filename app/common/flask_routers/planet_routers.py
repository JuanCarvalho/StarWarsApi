from flask import jsonify
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.factories import api_rest_factory

planets_ns = Namespace("planets", description="Planets operations")
api_rest_adapter: ApiRestContract = api_rest_factory.create("flaskapi_adapter")


@planets_ns.route("/")
class PlanetsResourceList(Resource):
    @planets_ns.doc(description="List all planets", responses={200: "Success"})
    def get(self):
        response = {
            "id": 1,
            "name": "Tatooine",
            "rotation_period": "23",
        }

        return jsonify([response, response])


@planets_ns.route("/<int:id>")
class PlanetsResourceGet(Resource):
    @planets_ns.doc(description="Get planet by id", responses={200: "Success", 404: "Planet not found"})
    def get(self, id: int):
        response = {
            "id": id,
            "name": "Tatooine",
            "rotation_period": "23",
        }
        return jsonify(response)

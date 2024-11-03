from flask import jsonify
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.factories import api_rest_factory

movies_ns = Namespace("movie", description="Planets operations")


@movies_ns.route("/")
class PlanetsResourceList(Resource):
    @movies_ns.doc(description="List all movies", responses={200: "Success"})
    def get(self):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
        response = api_rest_adapter.list()
        return jsonify([response, response])


@movies_ns.route("/<string:id>")
class PlanetsResourceGet(Resource):
    @movies_ns.doc(description="Get movie by id", responses={200: "Success", 404: "Planet not found"})
    def get(self, id: str):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
        response = api_rest_adapter.get(id)
        return jsonify(response)

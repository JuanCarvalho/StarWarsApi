from flask import jsonify, request
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.common.exceptions.api_exceptions import BadRequest
from app.factories import api_rest_factory

movies_ns = Namespace("movie", description="Planets operations")


@movies_ns.route("/")
class PlanetsResourceList(Resource):
    @movies_ns.doc(description="List all movies", responses={200: "Success"})
    def get(self):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
        return jsonify(api_rest_adapter.list())

    @movies_ns.doc(description="Create a new movie", responses={201: "Created"})
    def post(self):
        try:
            api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
            response = api_rest_adapter.create(request.json)  # type: ignore
            return response, 201
        except BadRequest as e:
            return {"message": str(e)}, 400


@movies_ns.route("/<string:id>")
class PlanetsResourceGet(Resource):
    @movies_ns.doc(description="Get movie by id", responses={200: "Success", 404: "Planet not found"})
    def get(self, id: str):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
        response = api_rest_adapter.get(id)
        return jsonify(response)

    @movies_ns.doc(description="Update movie by id", responses={200: "Success", 404: "Planet not found"})
    def put(self, id: str):
        try:
            api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="filmes")
            response = api_rest_adapter.update(id, request.json)  # type: ignore
            return response, 200
        except BadRequest as e:
            return {"message": str(e)}, 400

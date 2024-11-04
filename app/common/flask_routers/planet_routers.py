from flask import jsonify, request
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.common.exceptions.api_exceptions import BadRequest
from app.factories import api_rest_factory

planets_ns = Namespace("planet", description="Planets operations")


@planets_ns.route("/")
class PlanetsResourceList(Resource):
    @planets_ns.doc(description="List all planets", responses={200: "Success"})
    def get(self):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        return jsonify(api_rest_adapter.list())

    @planets_ns.doc(description="Create a new planet", responses={201: "Created"})
    def post(self):
        try:
            api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
            response = api_rest_adapter.create(request.json)  # type: ignore
            return response, 201
        except BadRequest as e:
            return {"message": str(e)}, 400


@planets_ns.route("/<string:id>")
class PlanetsResourceGet(Resource):
    @planets_ns.doc(description="Get planet by id", responses={200: "Success", 404: "Planet not found"})
    def get(self, id: str):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        response = api_rest_adapter.get(id)
        return jsonify(response)

    @planets_ns.doc(description="Update planet by id", responses={200: "Success", 404: "Planet not found"})
    def put(self, id: str):
        try:
            api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
            response = api_rest_adapter.update(id, request.json)  # type: ignore
            return response, 200
        except BadRequest as e:
            return {"message": str(e)}, 400

    @planets_ns.doc(description="Delete planet by id", responses={200: "Success", 404: "Planet not found"})
    def delete(self, id: str):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        response = api_rest_adapter.delete(id)
        return response, 200

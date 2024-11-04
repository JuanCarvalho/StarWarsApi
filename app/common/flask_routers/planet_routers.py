from flask import jsonify, request
from flask_restx import Namespace, Resource

from app.adapters.rest_api.rest_api_contract import ApiRestContract
from app.common.exceptions.api_exceptions import BadRequest
from app.common.schemas import PlanetCreateSchema
from app.factories import api_rest_factory
from app.utils.pydantic_to_flask_model import pydantic_to_flask_model

planets_ns = Namespace("planet", description="Planets operations")

# TODO: - Melhorar a documentação
#       - Adicionar os modelos esperados para os métodos POST e PUT
#       - Adicionar os modelos de resposta esperados para os métodos GET, POST, PUT e DELETE


planet_model = pydantic_to_flask_model(PlanetCreateSchema, planets_ns)


@planets_ns.route("/")
class PlanetsResourceList(Resource):
    @planets_ns.doc(description="List all planets", responses={200: "Success"})
    def get(self):
        api_rest_adapter: ApiRestContract = api_rest_factory.create("flask_api_adapter", table_name="planetas")
        return jsonify(api_rest_adapter.list())

    @planets_ns.doc(
        description="Create a new planet",
        responses={201: "Created"},
    )
    @planets_ns.expect(planet_model)
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

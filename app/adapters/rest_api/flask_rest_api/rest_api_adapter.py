from app.common.exceptions.api_exceptions import handle_errors_flaskapi
from app.config.logger import LOGGER
from app.factories import api_rest_factory, port_factory
from app.ports import CrudPortInput


@api_rest_factory.register("flask_api_adapter")
class FlaskApiAdapter:

    def __init__(self, table_name: str | None = None):
        self.crud_input_port: CrudPortInput = port_factory.create("crud_port_input", table_name=table_name)

    @handle_errors_flaskapi
    def health_check(self):
        LOGGER.info("Health check")
        return self.crud_input_port.health_check()

    @handle_errors_flaskapi
    def get(self, id: int, table_name: str):
        LOGGER.info(f"Get item with id {id}")
        return self.crud_input_port.get(id, table_name)

    @handle_errors_flaskapi
    def list(self, filters: dict | None = None):
        LOGGER.info(f"List items with filters {filters}")
        return self.crud_input_port.list(filters)

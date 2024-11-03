from app.common.exceptions.api_exceptions import handle_errors_fastapi
from app.config.logger import LOGGER
from app.factories import api_rest_factory, port_factory
from app.ports import CrudPortInput


@api_rest_factory.register("flaskapi_adapter")
class FlaskApiAdapter:
    crud_input_port: CrudPortInput = port_factory.create("crud_port_input")

    @handle_errors_fastapi
    def health_check(self):
        LOGGER.info("Health check")
        return self.crud_input_port.health_check()

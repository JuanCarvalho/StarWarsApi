from app.adapters import MongoDBRepository
from app.common.exceptions.api_exceptions import handle_errors_fastapi
from app.config.logger import LOGGER
from app.factories import api_rest_factory, repository_factory


@api_rest_factory.register("flaskapi_adapter")
class FlaskApiAdapter:

    @handle_errors_fastapi
    def health_check(self):
        db_reposiroty: MongoDBRepository = repository_factory.create("mongodb_repository")  # type: ignore
        LOGGER.info(f"{db_reposiroty.health_check_db()}")
        return {"status": "ok"}

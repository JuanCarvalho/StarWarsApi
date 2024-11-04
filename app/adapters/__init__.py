from typing import TYPE_CHECKING, List

from app.adapters.repository.mongo_db_repository.mongodb_repository import MongoDBRepository
from app.adapters.repository.nosql_repository_contract import NoSqlRepositoryContract
from app.adapters.rest_api.flask_rest_api.rest_api_adapter import FlaskApiAdapter
from app.adapters.rest_api.rest_api_contract import ApiRestContract

__all__ = [
    "FlaskApiAdapter",
    "MongoDBRepository",
    "ApiRestContract",
    "NoSqlRepositoryContract",
]

if TYPE_CHECKING:

    rest_api_gateway_db_adapter: List[ApiRestContract] = [FlaskApiAdapter()]
    nosql_repository_adapter: List[NoSqlRepositoryContract] = [MongoDBRepository()]

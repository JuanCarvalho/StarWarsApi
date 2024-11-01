from typing import Any, Dict

from app.factories.base_factory import BaseFactory


class RepositoryFactory(BaseFactory):
    """The factory class for creating repositories"""

    registry: Dict[str, Any] = {}
    registry_singleton: Dict[str, Any] = {}

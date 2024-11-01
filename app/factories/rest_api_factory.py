from typing import Any, Dict

from app.factories.base_factory import BaseFactory


class ApiRestFactory(BaseFactory):
    """The factory class for creating api_rest"""

    registry: Dict[str, Any] = {}
    registry_singleton: Dict[str, Any] = {}

from typing import Any, Dict

from app.factories.base_factory import BaseFactory


class DomainFactory(BaseFactory):
    """The factory class for creating ports"""

    registry: Dict[str, Any] = {}
    registry_singleton: Dict[str, Any] = {}

from typing import Any, Callable, Dict

from app.common.exceptions.factory_exceptions import FactoryError


class BaseFactory:
    """The abstract factory class for creating classes"""

    registry: Dict[str, Any] = {}
    registry_singleton: Dict[str, Any] = {}

    @classmethod
    def register(cls, factory_key: str) -> Callable:
        def inner_wrapper(wrapped_class: Callable) -> Callable:
            cls.registry[factory_key] = wrapped_class
            return wrapped_class

        return inner_wrapper

    @classmethod
    def create(cls, factory_key: str, **kwargs) -> Any:
        if factory_key not in cls.registry:
            raise FactoryError(factory_key)

        k_class = cls.registry[factory_key]
        i_class = k_class(**kwargs)
        return i_class

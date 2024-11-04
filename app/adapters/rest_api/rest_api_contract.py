from typing import Any, Protocol


class ApiRestContract(Protocol):

    def health_check(self) -> Any:
        pass

    def get(self, id: str) -> Any:
        pass

    def list(self, filters: dict | None = None) -> Any:
        pass

    def create(self, data: dict) -> Any:
        pass

    def update(self, id: str, data: dict) -> Any:
        pass

    def delete(self, id: str) -> Any:
        pass

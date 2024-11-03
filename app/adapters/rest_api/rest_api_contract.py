from typing import Any, Protocol


class ApiRestContract(Protocol):

    def health_check(self) -> Any:
        pass

    def get(self, id: int) -> Any:
        pass

    def list(self, filters: dict | None = None) -> Any:
        pass

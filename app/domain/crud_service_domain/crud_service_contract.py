from typing import Protocol


class CrudServiceContract(Protocol):

    def health_check(self) -> dict:
        pass

    def create(self, data: dict) -> dict:
        pass

    def update(self, id: str, data: dict) -> None:
        pass

    def delete(self, id: str) -> None:
        pass

    def get(self, id: str) -> dict:
        pass

    def list(self, filters: dict | None = None) -> dict:
        pass

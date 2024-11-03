from typing import Protocol


class CrudServiceContract(Protocol):

    def health_check(self) -> dict:
        pass

    def create(self, data: dict) -> dict:
        pass

    def update(self, data: dict) -> dict:
        pass

    def delete(self, id: int) -> None:
        pass

    def get(self, id: str) -> dict:
        pass

    def list(self, filters: dict | None = None) -> dict:
        pass

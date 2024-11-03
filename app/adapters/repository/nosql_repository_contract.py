from typing import Protocol


class NoSqlRepositoryContract(Protocol):

    def health_check(self) -> dict:
        pass

    def get(self, id: int) -> dict:
        pass

    def list(self, filters: dict | None = None) -> dict:
        pass

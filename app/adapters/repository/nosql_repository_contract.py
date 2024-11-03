from typing import Protocol


class NoSqlRepositoryContract(Protocol):

    def health_check(self) -> dict:
        pass

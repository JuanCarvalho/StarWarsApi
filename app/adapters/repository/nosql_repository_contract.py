from typing import Protocol


class NoSqlRepositoryContract(Protocol):

    def health_check_db(self) -> dict:
        pass

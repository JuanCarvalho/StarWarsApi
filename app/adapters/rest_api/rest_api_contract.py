from typing import Any, Protocol


class ApiRestContract(Protocol):

    def health_check(self) -> Any:
        pass

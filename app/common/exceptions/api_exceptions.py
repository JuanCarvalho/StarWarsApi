from functools import wraps
from typing import Optional

from app.config.logger import LOGGER


class CustomException(Exception):
    def __init__(self, message: Optional[str] = None):
        self.message = message


class BadRequest(CustomException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)


def handle_errors_flaskapi(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequest as e:
            LOGGER.error(f"Erro customizado - {e.message}")
            raise BadRequest(e.message)
        except Exception as e:
            LOGGER.error("Erro desconhecido")
            raise Exception(str(e))  # Aplicar http error do flask

    return wrapper

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional, Union

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.common.schemas.planet_schema import PlanetCreateSchema


class MoviesSchema(BaseModel):
    id: str
    titulo: str
    data_lancamento: str
    diretor: str
    planetas: List[str | None]
    data_criacao: datetime
    data_ultima_alteracao: datetime

    @classmethod
    def from_mongo(cls, data: dict):
        data["id"] = str(data["_id"])
        planetas = data.get("planetas") or []
        data["planetas"] = [str(planeta_id) for planeta_id in planetas]
        return cls(**data)


class MoviesCreateSchema(BaseModel):
    titulo: str
    data_lancamento: str
    diretor: str
    planetas: Optional[List[Union[str, "PlanetCreateSchema"]]] = None


class MoviesUpdateSchema(BaseModel):
    titulo: Optional[str] = None
    data_lancamento: Optional[str] = None
    diretor: Optional[str] = None
    planetas: Optional[List[str]] = None

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional, Union

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.common.schemas.movies_schema import MoviesCreateSchema


class PlanetSchema(BaseModel):
    id: str
    nome: str
    clima: str
    diametro: int
    populacao: int
    filmes: List[str]  # Modificação para representar os ObjectIds como strings
    data_criacao: datetime
    data_ultima_alteracao: datetime

    @classmethod
    def from_mongo(cls, data: dict):
        data["id"] = str(data["_id"])
        data["filmes"] = [str(filme_id) for filme_id in data.get("filmes", [])]
        return cls(**data)


class PlanetCreateSchema(BaseModel):
    nome: str
    clima: str
    diametro: int
    populacao: int
    filmes: Optional[List[Union[str, "MoviesCreateSchema"]]] = None


class PlanetUpdateSchema(BaseModel):
    nome: Optional[str] = None
    clima: Optional[str] = None
    diametro: Optional[int] = None
    populacao: Optional[int] = None
    filmes: Optional[List[Union[str, "MoviesCreateSchema"]]] = None

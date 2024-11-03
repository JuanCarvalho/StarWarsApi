from datetime import datetime
from typing import List

from pydantic import BaseModel


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

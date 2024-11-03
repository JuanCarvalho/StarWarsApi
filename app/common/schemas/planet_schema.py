from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel


class PlanetSchema(BaseModel):
    _id: str
    nome: str
    clima: str
    diametro: int
    populacao: int
    filmes: List[str]  # Modificação para representar os ObjectIds como strings
    data_criacao: datetime
    data_ultima_alteracao: datetime

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data: dict):
        # Converte os ObjectIds na lista 'filmes' para strings
        data["_id"] = str(data["_id"])
        data["filmes"] = [str(filme_id) for filme_id in data.get("filmes", [])]
        return cls(**data)

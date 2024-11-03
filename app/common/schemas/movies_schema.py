from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel


class MoviesSchema(BaseModel):
    id: str
    titulo: str
    data_lancamento: str
    diretor: str
    planetas: List[str]
    data_criacao: datetime
    data_ultima_alteracao: datetime

    @classmethod
    def from_mongo(cls, data: dict):
        data["id"] = str(data["_id"])
        data["planetas"] = [str(planeta_id) for planeta_id in data.get("planetas", [])]
        return cls(**data)

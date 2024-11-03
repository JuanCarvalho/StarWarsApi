# filmes_schema.py
from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel


class PlanetRef(BaseModel):
    _id: str

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}


class MoviesSchema(BaseModel):
    _id: str
    titulo: str
    data_lancamento: str
    diretor: str
    planetas: List[PlanetRef]
    data_criacao: datetime
    data_ultima_alteracao: datetime

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}

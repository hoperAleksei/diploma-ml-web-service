from typing import List

from pydantic import BaseModel
from enum import Enum
from pandas import DataFrame

class State(Enum):
    ready = "ready" # до загрузки выборки
    prepro = "prepro" # на экране предобработки
    split = "split" # на экране разбиения
    autofit = "autofit" # на экране выбора алгоритмов

class Prepro(BaseModel):
    pass

class Split(BaseModel):
    pass

class Autofit(BaseModel):
    pass

class UserState(BaseModel):
    state: State = State.ready # состояние эксперимента
    name: str | None = None # название эксперимента
    dataset_id: int # идентификатор выборки
    dataset: DataFrame | None = None # предобработанная выборка
    splits: List[Split] = [] # разбиения
    autofit: List[Autofit] = [] # алгоритмы и их настройки

    class Config:
        arbitrary_types_allowed = True

from typing import List

from pydantic import BaseModel
from enum import Enum
from pandas import DataFrame


class State(Enum):
    ready = "ready"  # до задания названия эксперимента
    start = "start"  # до загрузки выборки, есть название эксперимента
    prepro = "prepro"  # на экране предобработки, есть выборка
    split = "split"  # на экране разбиения, есть параметры предобработки
    autofit = "autofit"  # на экране выбора алгоритмов, есть параметры разбиения


class Experiment(BaseModel):
    name: str


class ExperimentInDB(Experiment):
    id: int


class Split(BaseModel):
    pass


class Autofit(BaseModel):
    pass


class UserState(BaseModel):
    state: State = State.ready  # состояние эксперимента
    name: str | None = None  # название эксперимента
    dataset_id: int | None = None  # идентификатор выборки
    dataset: DataFrame | None = None  # предобработанная выборка
    splits: List[Split] = []  # разбиения
    autofit: List[Autofit] = []  # алгоритмы и их настройки

    class Config:
        arbitrary_types_allowed = True


class ReturnUserState(BaseModel):
    state: State
    name: str = ""

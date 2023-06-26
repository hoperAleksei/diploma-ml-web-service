from typing import List

from pydantic import BaseModel
from enum import Enum
from pandas import DataFrame

class State(Enum):
    ready = "ready"
    prepro = "prepro"
    split = "split"
    autofit = "autofit"

class Prepro(BaseModel):
    pass

class Split(BaseModel):
    pass

class Autofit(BaseModel):
    pass

class UserState(BaseModel):
    state: State = State.ready
    dataset_id: int
    dataset: DataFrame | None = None
    splits: List[Split] = []
    autofit: List[Autofit] = []

    class Config:
        arbitrary_types_allowed = True

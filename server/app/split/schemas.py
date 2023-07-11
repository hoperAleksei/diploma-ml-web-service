from enum import Enum

from pydantic import BaseModel


class Yeno(Enum):
    yes = "yes"
    no = "no"


class Split(BaseModel):
    ts: int
    rs: int
    st: Yeno

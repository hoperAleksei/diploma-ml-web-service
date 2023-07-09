from pydantic import BaseModel
from typing import Any

class Dataset(BaseModel):
    id: int
    name: str | None = None


class Url(BaseModel):
    url: str


class SampleTable(BaseModel):
    names: list[str]
    types: list[str]
    lines: list[list[Any]]

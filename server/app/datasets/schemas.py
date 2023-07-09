from pydantic import BaseModel


class Dataset(BaseModel):
    id: int
    name: str | None = None


class Url(BaseModel):
    url: str

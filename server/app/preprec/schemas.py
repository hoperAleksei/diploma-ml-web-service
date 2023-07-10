from pydantic import BaseModel


class Method(BaseModel):
    name: str
    nm: str


class Pre(BaseModel):
    type: str
    name: str
    desc: str
    methods: list[Method] | None = None
    value: str | None = None


class PreSend(BaseModel):
    label: str
    op: str | None = None
    ec: str | None = None
    nd: str | None = None
    ov: str | None = None
    sa: str | None = None
    de: list | None = None
    tn: list | None = None

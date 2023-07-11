from sqlalchemy import Table, Column, String, Integer, ForeignKey

from database import metadata

requirement = Table(
    "requirement",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
)

algorithm = Table(
    "algorithm",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, default=""),
)

alg_req = Table(
    "alg_req",
    metadata,
    Column("pre_id", Integer, ForeignKey("requirement.id"), primary_key=True),
    Column("alg_id", Integer, ForeignKey("algorithm.id"), primary_key=True),
)

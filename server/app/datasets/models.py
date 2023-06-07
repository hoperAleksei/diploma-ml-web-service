from sqlalchemy import Table, Column, String, Integer

from database import metadata

dataset = Table(
    "dataset",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
)

from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

test = Table(
    "test",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)
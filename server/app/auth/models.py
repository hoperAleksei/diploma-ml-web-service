from sqlalchemy import Table, Column, String

from database import metadata

user = Table(
    "user",
    metadata,
    Column("username", String, primary_key=True),
    Column("hashed_password", String, nullable=False),
    Column("role", String, nullable=False, default="user")
)

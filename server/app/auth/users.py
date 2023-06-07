from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, Row
from sqlalchemy.exc import IntegrityError

from database import async_session_maker
from .schemas import User, UserInDB
from .models import user


async def get_user(username: str) -> UserInDB | None:
    query = select(user).where(user.c.username == username)

    async with async_session_maker() as session:
        result = await session.execute(query)

    users = result.all()

    if len(users) == 0:
        return None
    else:
        return UserInDB(**users[0]._mapping)

async def add_user(user_in_db: UserInDB) -> bool:

    stmt = insert(user).values(
        username = user_in_db.username,
        hashed_password = user_in_db.hashed_password,
        role = user_in_db.role.value
    )

    async with async_session_maker() as session:
        try:
            await session.execute(stmt)
            await session.commit()
            return True
        except IntegrityError as e:
            # username already in use
            return False

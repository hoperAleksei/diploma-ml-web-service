import os
import aiofiles

from fastapi import UploadFile
from fastapi.exceptions import HTTPException

from sqlalchemy import insert, select

from database import async_session_maker
from .models import dataset

import pandas

DATASETS_PATH = os.path.join(os.path.abspath("."), "datasets")

async def create_dataset(name: str):
    stmt = insert(dataset).values(
        name = name
    )
    async with async_session_maker() as session:
        await session.execute(stmt)
        await session.commit()

async def is_exist_dataset(name: str):
    query = select(dataset).where(dataset.c.name == name)
    async with async_session_maker() as session:
        result = await session.execute(query)
    if len(result.all()) == 0:
        return False
    else:
        return True

async def save_dataset(file: UploadFile):
    if os.path.exists(DATASETS_PATH) and os.path.isdir(DATASETS_PATH):
        pass
    else:
        os.mkdir(DATASETS_PATH)

    try:
        pandas.read_csv(file.file)
    except:
        pass
    file.file.seek(0)
    if os.path.exists(os.path.join(DATASETS_PATH, file.filename)):
        raise HTTPException(409, detail="file already exist")
    else:
        async with aiofiles.open(os.path.join(DATASETS_PATH, file.filename), "wb") as out:
            inp = await file.read()
            await out.write(inp)
        await create_dataset(file.filename)

async def get_datasets():
    query = select(dataset).where(dataset.c.name == "iris.csv")
    async with async_session_maker() as session:
        result = await session.execute(query)
    return result.all()

async def load_dataset(name: str) -> pandas.DataFrame:
    ied = await is_exist_dataset(name)
    if ied and os.path.exists(os.path.join(DATASETS_PATH, name)):
        return pandas.read_csv(os.path.join(DATASETS_PATH, name))


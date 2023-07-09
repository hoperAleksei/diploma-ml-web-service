import os
import urllib

import sqlalchemy
import wget
import tempfile

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
        name=name
    )
    async with async_session_maker() as session:
        await session.execute(stmt)
        try:
            await session.commit()
        except Exception as e:
            raise HTTPException(409, detail="file already exist")


async def is_exist_dataset(dataset_id: int):
    query = select(dataset).where(dataset.c.id == dataset_id)
    async with async_session_maker() as session:
        result = await session.execute(query)
    if len(result.all()) == 0:
        return False
    else:
        return True


async def save_url(url: str):
    try:
        filename = wget.filename_from_url(url)
        file = urllib.request.urlopen(url)
    except Exception as e:
        raise HTTPException(404, detail="file not found")
    await save_dataset(UploadFile(file, filename=filename))


async def save_dataset(file: UploadFile):
    # print({"file": file.file, "m": file.filename})
    filename = file.filename
    with tempfile.TemporaryFile() as f:
        f.write(file.file.read())
        f.seek(0)
        # проверка на наличие директории с выборками
        if not (os.path.exists(DATASETS_PATH) and os.path.isdir(DATASETS_PATH)):
            os.mkdir(DATASETS_PATH)

        try:
            pandas.read_csv(f)
        except:
            raise HTTPException(409, detail="file is not dataset")
        f.seek(0)
        if os.path.exists(os.path.join(DATASETS_PATH, filename)):
            raise HTTPException(409, detail="file already exist")
        else:
            async with aiofiles.open(os.path.join(DATASETS_PATH, filename), "wb") as out:
                inp = f.read()
                await out.write(inp)
            await create_dataset(filename)


async def get_datasets():
    query = select(dataset)
    async with async_session_maker() as session:
        result = await session.execute(query)
    return result.all()


async def get_dataset_name(dataset_id: int):
    query = select(dataset.c.name).where(dataset.c.id == dataset_id)
    async with async_session_maker() as session:
        result = await session.execute(query)
    return result.first()[0]


async def load_dataset(dataset_id: int) -> pandas.DataFrame | None:
    ied = await is_exist_dataset(dataset_id)
    if ied:
        dataset_name = await get_dataset_name(dataset_id)
        dataset_path = os.path.join(DATASETS_PATH, dataset_name)
        if os.path.exists(dataset_path):
            return pandas.read_csv(dataset_path)
    else:
        raise HTTPException(404, detail="dataset not found")

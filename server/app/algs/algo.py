import os

import aiofiles
from external import experimentation
from external import preprocessing

import external

from fastapi import UploadFile, HTTPException

from sqlalchemy import insert, select

from .schemas import ParseOut
from .models import algorithm, requirement, alg_req
from database import async_session_maker

run_experiments = external.experimentation.run_experiments
algs_loader = external.experimentation.algs_loader
get_all_algs_req = external.experimentation.get_all_algs_req
get_all_alg = external.experimentation.get_all_alg
parse = external.experimentation.parse

list_alg = external.preprocessing.list_alg
sample_split = external.preprocessing.sample_split

TEST_PATH = os.path.join(os.path.abspath("."), "experimentation", "test")
ALGS_PATH = os.path.join(os.path.abspath("."), "experimentation", "algs")

import os


async def get_req_id(name: str):
    query = select(requirement.c.id).where(requirement.c.name == name)
    async with async_session_maker() as session:
        result = await session.execute(query)
    if result:
        return result.first()[0]
    else:
        raise Exception("not in reqs")


async def create_alg(name: str, desc: str, pres: list[str]):
    stmt = insert(algorithm).values(
        name=name,
        description=desc
    ).returning(algorithm.c.id)
    async with async_session_maker() as session:
        alg_id = (await session.execute(stmt)).first()[0]
        for p in pres:
            pre_id = await get_req_id(p)
            stmt = insert(alg_req).values(
                alg_id=alg_id,
                pre_id=pre_id
            )
            await session.execute(stmt)
        try:
            await session.commit()
        except Exception as e:
            raise HTTPException(400, detail="db Error")

async def get_algs():
    query = select(algorithm)
    async with async_session_maker() as session:
        result = await session.execute(query)
    return [x._mapping for x in result.all()]


async def loadAlg(file: UploadFile):
    filename: str = file.filename
    alg_name: str = filename.split(".")[0]

    test_file_path = os.path.join(TEST_PATH, filename)
    alg_file_path = os.path.join(ALGS_PATH, filename)

    async with aiofiles.open(test_file_path, "wb") as out:
        inp = file.file.read()
        await out.write(inp)

    ans = parse(alg_name)

    if ans.status:
        try:
            await create_alg(name=ans.name, desc=ans.desc, pres=ans.pre)

            file.file.seek(0)
            async with aiofiles.open(alg_file_path, "wb") as out:
                inp = file.file.read()
                await out.write(inp)
        except Exception:
            raise HTTPException(409, detail="File already exist")

        os.remove(test_file_path)
    else:
        os.remove(test_file_path)

        return HTTPException(400, detail=ans.details)

    return True

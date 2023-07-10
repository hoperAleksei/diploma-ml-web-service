import os

import aiofiles
from external import experimentation

import external
from fastapi import UploadFile

from .schemas import ParseOut

run_experiments = external.experimentation.run_experiments
algs_loader = external.experimentation.algs_loader
get_all_algs_req = external.experimentation.get_all_algs_req
get_all_alg = external.experimentation.get_all_alg
parse = external.experimentation.parse

TEST_PATH = os.path.join(os.path.abspath("."), "experimentation", "test")

import os

async def loadAlg(file: UploadFile) -> ParseOut:
    filename: str = file.filename

    async with aiofiles.open(os.path.join(TEST_PATH, filename), "wb") as out:
        inp = file.file.read()
        await out.write(inp)

    ans = parse(filename.split(".")[0])

    return ans



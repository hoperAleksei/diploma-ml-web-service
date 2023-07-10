from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from sklearn.datasets import load_iris

from .schemas import ExperimentResultInput, ExperimentResultOutput, ParseOut, Param
from .algo import get_all_alg, loadAlg, run_experiments

import globals

from state_manager.schemas import State

router = APIRouter(
    prefix="/api/alg",
    tags=["Algorithms"]
)


@router.post("/test")
async def test(file: UploadFile):
    res = await loadAlg(file)
    return res


@router.post("/test123")
async def test123():
    return get_all_alg(["k-nearest neighbors"])


@router.get("test")
async def get_test():
    iris = load_iris()
    return run_experiments([ExperimentResultInput(alg_name='k-nearest neighbors', n_steps=3,
                                                 params=[Param(name="n_neighbors", type="int", min=1, max=2),
                                                         Param(name="weights", type="set", values=["uniform"])])], iris.data,
                           iris.target, iris.data, iris.target)

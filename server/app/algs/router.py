from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from sklearn.datasets import load_iris

from .schemas import ExperimentResultInput, ExperimentResultOutput, ParseOut, Param
from .algo import get_all_alg, loadAlg, run_experiments, create_alg, get_algs, list_alg, get_all_algs_req

import globals

from state_manager.schemas import State

router = APIRouter(
    prefix="/api/alg",
    tags=["Algorithms"]
)


@router.post("")
async def alg_upload(
        file: UploadFile,
        current_user: User = Depends(get_current_user)
):
    res = await loadAlg(file)
    if res:
        return {"status": "ok"}
    else:
        HTTPException(400, "Something went wrong")


@router.get("")
async def alg_get(
        current_user: User = Depends(get_current_user)
):
    return await get_algs()


@router.get("/available")
async def get_available(
        current_user: User = Depends(get_current_user)
):
    try:
        state = globals.state[current_user.username]
        ds = state.dataset

        return list_alg(ds, get_all_algs_req())

    except KeyError:
        return HTTPException(
            400,
            detail="not correct"
        )


@router.get("test")
async def get_test():
    ...
    # iris = load_iris()
    # return run_experiments([ExperimentResultInput(alg_name='k-nearest neighbors', n_steps=3,
    #                                              params=[Param(name="n_neighbors", type="int", min=1, max=2),
    #                                                      Param(name="weights", type="set", values=["uniform"])])], iris.data,
    #                        iris.target, iris.data, iris.target)

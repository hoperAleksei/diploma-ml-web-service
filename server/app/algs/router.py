from enum import Enum

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from sklearn.datasets import load_iris

from split.schemas import Split

from .schemas import ExperimentResultInput, ExperimentResultOutput, ParseOut, Param
from .algo import get_all_alg, loadAlg, run_experiments, create_alg, get_algs, list_alg, get_all_algs_req, sample_split

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
        HTTPException(400, detail="Something went wrong")


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

        res = list_alg(ds, get_all_algs_req())

        return [{"name": list(r.keys())[0], "status": list(r.values())[0]} for r in res]

    except KeyError:
        return HTTPException(
            400,
            detail="not correct"
        )


@router.get("/to_run")
async def get_to_run(
        current_user: User = Depends(get_current_user)
):
    try:
        state = globals.state[current_user.username]
        ds = state.dataset

        res = get_all_alg([list(a.keys())[0] for a in list_alg(ds, get_all_algs_req())])

        return res

    except KeyError:
        return HTTPException(
            400,
            detail="not correct"
        )


@router.post("/run")
async def run_experiment(
        autofit_params: list[ExperimentResultInput],
        current_user: User = Depends(get_current_user)
):
    state = globals.state[current_user.username]
    ds = state.dataset
    exp_name = state.name
    splits_params = state.splits

    sp = []

    for s in splits_params:
        tmp = s.model_dump(exclude_none=True, exclude_unset=True)
        tmp["st"] = None

        sp.append(tmp)

    splits = sample_split(sp, ds)

    ress = []

    for s in splits:
        ress.append(run_experiments(autofit_params, s["trainX"], s["trainY"], s["testX"], s["testY"]))

    print(ress)


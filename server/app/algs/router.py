from enum import Enum

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from pydantic import BaseModel
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

        print(get_all_algs_req())

        res = list_alg(ds, get_all_algs_req())
        print(res)

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

        a = [list(a.keys())[0] for a in list_alg(ds, get_all_algs_req()) if list(a.values())[0] == 'ok']
        print("===============", a)

        res = get_all_alg(a)

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
    username = current_user.username
    state = globals.state[username]
    ds = state.dataset
    exp_name = state.name
    splits_params = state.splits

    sp = []
    spp = []

    for s in splits_params:
        tmp = s.model_dump(exclude_none=True, exclude_unset=True)
        spp.append(tmp)
        tmp["st"] = None

        sp.append(tmp)

    splits = sample_split(sp, ds)

    ress = []

    for (i, s) in enumerate(splits):
        ress.append(
            {"name": exp_name, "split": spp[i], "exps": run_experiments(autofit_params, s["trainX"], s["trainY"], s["testX"], s["testY"])})

    if username not in globals.results.keys():
        globals.results[username] = [ress]
        idd = 0
    else:
        globals.results[username].append(ress)
        idd = len(globals.results[username]) - 1

    globals.state.pop(username, None)
    print(globals.results[username])

    return {"status": "ok", "id": idd}

@router.get("/exps")
async def get_experiments(
        current_user: User = Depends(get_current_user)
):
    results = globals.results[current_user.username]
    # print([{"id": i, "name": v[0]["name"]} for i, v in enumerate(results)])
    return [{"id": i, "name": v[0]["name"]} for i, v in enumerate(results)]
    # return {"id": i, "name": name


class Idd(BaseModel):
    id: int


@router.post("/result")
async def run_experiment(
        idd: Idd,
        current_user: User = Depends(get_current_user)
):
    return globals.results[current_user.username][idd.id]

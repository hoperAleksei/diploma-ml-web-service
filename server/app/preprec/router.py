from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user

from .proc import PRE_TYPES, prepr
from .schemas import PreSend

import globals

from state_manager.schemas import State

router = APIRouter(
    prefix="/api/pre",
    tags=["Preprocessing"]
)


@router.get("/types")
async def get_pre_types(
        current_user: User = Depends(get_current_user)
):
    return PRE_TYPES


@router.post("")
async def preprocess_dataset(
        methods: PreSend,
        current_user: User = Depends(get_current_user)
):
    met = methods.model_dump(exclude_none=True, exclude_unset=True)
    try:

        state = globals.state[current_user.username]
        ds = state.dataset

        res = prepr(ds, met)

        state.dataset = res

    except KeyError:
        raise HTTPException(
            status_code=409,
            detail="user is not preprocessing"
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="label is not in dataset"
        )

    return {"status": "ok"}


@router.post("/commit")
def preprocess_commit(
        current_user: User = Depends(get_current_user)
):
    try:
        state = globals.state[current_user.username]

        if state.state == State.prepro:
            state.state = State.split
        else:
            raise HTTPException(
                status_code=409,
                detail="user is not preprocessing"
            )

    except KeyError:
        raise HTTPException(
            status_code=409,
            detail="user is not experimenting"
        )

    return {"status": "ok"}


@router.get("/algs")
async def get_algorithms(
        current_user: User = Depends(get_current_user)
):
    """
    return {
        "name": "имя алгоритма",
        "state": true, если доступен
    }
    """
    # TODO
    pass

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user

from .schemas import Split

import globals

from state_manager.schemas import State

router = APIRouter(
    prefix="/api/split",
    tags=["Splitting"]
)


@router.post("")
def set_splits(
        splits: list[Split],
        current_user: User = Depends(get_current_user)
):
    try:
        state = globals.state[current_user.username]

        if state.state == State.split:
            if len(splits) <= 0 or len(splits) > 3:
                raise ValueError()
            state.splits = splits
            state.state = State.autofit
        else:
            raise KeyError()
    except KeyError:
        raise HTTPException(
            status_code=409,
            detail="user is not splitting"
        )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="splits are not valid"
        )
    return {"status": "ok"}

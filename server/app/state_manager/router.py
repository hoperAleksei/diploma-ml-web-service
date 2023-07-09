from fastapi import APIRouter, Depends, HTTPException

from auth.schemas import User
from auth.security import get_current_user
from .schemas import State, Experiment, UserState, ReturnUserState

import globals

router = APIRouter(
    prefix="/api/state",
    tags=["States"]
)

@router.get("", response_model=ReturnUserState)
async def get_state(user: User = Depends(get_current_user)):
    if user.username not in globals.state:
        return ReturnUserState(state=State.ready)
    else:
        user_state = globals.state[user.username]
        return ReturnUserState(state=user_state.state, name=user_state.name)

@router.post("/experiment")
async def start_experiment(experiment: Experiment, user: User = Depends(get_current_user)):
    if user.username not in globals.state:
        globals.state[user.username] = UserState()

    if globals.state[user.username].state == State.ready:
        globals.state[user.username].state = State.start
        globals.state[user.username].name = experiment.name
    else:
        raise HTTPException(
            status_code=409,
            detail="User already start experiment"
        )

@router.delete("/experiment")
async def cancel_experiment(user: User = Depends(get_current_user)):
    globals.state.pop(user.username, None)

    return {"status": "ok"}

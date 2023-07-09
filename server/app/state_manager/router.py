from fastapi import APIRouter, Depends

from auth.schemas import User
from auth.security import get_current_user
from .schemas import State

import globals

router = APIRouter(
    prefix="/api/state",
    tags=["States"]
)

@router.get("", response_model=State)
async def get_state(user: User = Depends(get_current_user)):
    if user.username not in globals.state:
        return State.ready
    else:
        return globals.state[user].state

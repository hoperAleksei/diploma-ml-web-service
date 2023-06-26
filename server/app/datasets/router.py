from typing import List

from fastapi import APIRouter, Depends
from fastapi import UploadFile

from auth.schemas import User
from auth.security import get_current_user
from state_manager.schemas import UserState

from .dataset import save_dataset, get_datasets, load_dataset
from .schemas import Dataset

import globals


router = APIRouter(
    prefix="/api/ds",
    tags=["Datasets"]
)


@router.post("/upload_file")
async def upload_dataset_from_file(
        file: UploadFile = Depends(save_dataset),
        current_user: User = Depends(get_current_user)
):
    return {"status": "ok"}


@router.post("/upload_url")
async def upload_dataset_from_url(
        url: str,
        current_user: User = Depends(get_current_user)
):
    raise NotImplementedError


@router.get("/get_datasets", response_model=List[Dataset]) # , response_model=List[Dataset]
async def get_datasets_from_db(
        current_user: User = Depends(get_current_user)
):
    return [x._mapping for x in await get_datasets()]


@router.get("/use_dataset")
async def use_dataset(
        dataset_id: int,
        current_user: User = Depends(get_current_user)
):
    if dataset_id not in globals.datasets:
        dataset = await load_dataset(dataset_id)
        globals.datasets[dataset_id] = dataset
    else:
        dataset = globals.datasets[dataset_id]

    if current_user.username not in globals.state:
        globals.state[current_user.username] = UserState(dataset_id=dataset_id, dataset=dataset.copy())
    else:
        globals.state[current_user.username].dataset_id = dataset_id
    return {"status": "ok"}

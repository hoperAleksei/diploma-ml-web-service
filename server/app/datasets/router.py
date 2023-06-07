import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from .dataset import save_dataset, get_datasets, load_dataset
from typing import List
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


@router.get("/get_datasets") # , response_model=List[Dataset]
async def get_datasets_from_db(
        current_user: User = Depends(get_current_user)
):
    return [x._mapping for x in await get_datasets()]


@router.get("/use_dataset")
async def use_dataset(
        dataset_name: str,
        current_user: User = Depends(get_current_user)
):
    if dataset_name not in globals.datasets:
        globals.datasets[dataset_name] = await load_dataset(dataset_name)
    if current_user.username not in globals.users:
        globals.users[current_user.username] = {"dataset": dataset_name}
    else:
        globals.users[current_user.username]["dataset"] = dataset_name

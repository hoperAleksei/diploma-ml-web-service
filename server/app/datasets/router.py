from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile

from auth.schemas import User
from auth.security import get_current_user
from state_manager.schemas import UserState, State

from .dataset import save_dataset, get_datasets, load_dataset, save_url, get_ds_table
from .schemas import Dataset, Url, SampleTable

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
        url: Url,
        current_user: User = Depends(get_current_user)
):
    await save_url(url.url)
    return {"status": "ok"}


@router.get("/get_datasets", response_model=List[Dataset])  # , response_model=List[Dataset]
async def get_datasets_from_db(
        current_user: User = Depends(get_current_user)
):
    return [x._mapping for x in await get_datasets()]


@router.post("/use_dataset")
async def use_dataset(
        ds: Dataset,
        current_user: User = Depends(get_current_user)
):
    try:
        user_state = globals.state[current_user.username]
    except KeyError:
        raise HTTPException(
            status_code=409,
            detail="User is not start experiment"
        )
    if user_state.state == State.start:
        dataset_id = ds.id
        if dataset_id not in globals.datasets:
            dataset = await load_dataset(dataset_id)
            globals.datasets[dataset_id] = dataset
        else:
            dataset = globals.datasets[dataset_id]

        user_state.dataset_id = dataset_id
        user_state.dataset = dataset.copy()
        user_state.state = State.prepro
        return {"status": "ok"}
    else:
        raise HTTPException(
            status_code=409,
            detail="User use dataset experiment"
        )


@router.get("/get_use", response_model=SampleTable)
async def get_user_dataset(
        current_user: User = Depends(get_current_user)
):
    try:
        state = globals.state[current_user.username]
        ds = state.dataset

        return await get_ds_table(ds)

    except KeyError:
        raise HTTPException(
            status_code=409,
            detail="User not use dataset"
        )

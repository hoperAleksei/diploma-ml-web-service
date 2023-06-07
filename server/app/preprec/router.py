from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile

from auth.schemas import User
from auth.security import get_current_user
from .proc import PRE_TYPES, prepr

router = APIRouter(
    prefix="/api/prep",
    tags=["Preprocessing"]
)


@router.get("/get_pre_types")
async def upload_dataset_from_file(
        current_user: User = Depends(get_current_user)
):
    return PRE_TYPES

@router.post("preproces_ds")
async def preproces_dataset(
        methods: dict,
        current_user: User = Depends(get_current_user)
):
    res = await prepr(current_user, methods)
    return res

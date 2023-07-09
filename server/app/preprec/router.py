from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile
from auth.schemas import User
from auth.security import get_current_user
from .proc import PRE_TYPES, prepr
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
import pandas as pd

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
def preproces_dataset(
        methods: dict,
        current_user: User = Depends(get_current_user)
):
    res = prepr(current_user, methods)
    return res


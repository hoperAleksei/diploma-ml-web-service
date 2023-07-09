import uvicorn

from fastapi import FastAPI, Request, status, Depends
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.middleware.cors import CORSMiddleware

from auth.router import router as auth_router
from datasets.router import router as datasets_router
from preprec.router import router as preprec_router
from state_manager.router import router as sm_router

app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")

app.include_router(auth_router)
app.include_router(datasets_router)
app.include_router(preprec_router)
app.include_router(sm_router)

origins = [
    "http://localhost",
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=["172.21.0.6", "http://localhost/login"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

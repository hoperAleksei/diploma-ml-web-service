import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from auth.router import router as auth_router


app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")

app.include_router(auth_router)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/api/test")
def read_root():
    return "hello"


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

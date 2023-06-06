import uvicorn

from fastapi import FastAPI

from auth.router import router as auth_router


app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")

app.include_router(auth_router)

import sys

@app.get("/api/test")
def read_root():
    return sys.path


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

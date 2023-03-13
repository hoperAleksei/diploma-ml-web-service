from typing import Union

import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc",
              openapi_url="/api/openapi.json")

@app.get("/api/")
def read_root():
    return {"Hello": "world"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

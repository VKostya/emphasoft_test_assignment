import uvicorn
from fastapi import FastAPI
from api.auth_api import auth_router
from api.service_api import service_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(service_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

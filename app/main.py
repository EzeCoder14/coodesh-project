from fastapi import FastAPI
from app.routers import integrate

app = FastAPI(title="Coodesh-project")

app.include_router(integrate.router)


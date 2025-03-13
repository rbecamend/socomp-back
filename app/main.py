from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.routes import router

app = FastAPI(title="Socomp API", version="1.0")

app.include_router(router)

@app.on_event("startup")
async def startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "A API Socomp está rodando!"}
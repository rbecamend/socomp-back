from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Socomp API", version="1.0")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "A API Socomp está rodando!"}
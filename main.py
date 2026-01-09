from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API de Análise de Vendas")

app.include_router(router)

@app.get("/")
def home():
    return {"status": "API rodando"}

from fastapi import APIRouter
from app.services import ler_vendas

router = APIRouter()

@router.get("/vendas")
def listar_vendas():
    return ler_vendas()

@router.get("/vendas/total")
def total_vendas():
    vendas = ler_vendas()
    total = 0
    for v in vendas:
        total += v["valor"] * v["quantidade"]
    return {"total_vendas": total}

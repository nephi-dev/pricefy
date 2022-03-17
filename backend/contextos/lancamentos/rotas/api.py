from typing import List
from uuid import UUID
from fastapi import APIRouter
from contextos.lancamentos.rotas.esquemas import LancamentoRetorno, LancamentoEntrada


router_lancamentos = APIRouter(tags=["Lançamentos"])


@router_lancamentos.post("/", response_model=LancamentoRetorno, status_code=201)
async def adicionar_lancamento(lancamento: LancamentoEntrada):
    pass


@router_lancamentos.patch("/{id}", response_model=LancamentoRetorno)
async def modificar_lancamento(id: UUID, lancamento: LancamentoEntrada):
    pass


@router_lancamentos.delete("/{id}", status_code=204)
async def deletar_lancamento(id: UUID):
    pass


@router_lancamentos.get("/", response_model=List[LancamentoRetorno])
async def visualizar_lancamentos():
    pass


@router_lancamentos.get("/{id}", response_model=LancamentoRetorno)
async def visualizar_lancamento_por_id(id: UUID):
    pass

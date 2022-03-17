from typing import List
from uuid import UUID
from fastapi import APIRouter
from contextos.estabelecimentos.rotas.esquemas import (
    EstabelecimentoRetorno,
    EstabelecimentoEntrada,
)


router_estabelecimentos = APIRouter(tags=["Estabelecimentos"])


@router_estabelecimentos.post(
    "/", response_model=EstabelecimentoRetorno, status_code=201
)
async def adicionar_estabelecimento(estabelecimento: EstabelecimentoEntrada):
    pass


@router_estabelecimentos.patch("/{id}", response_model=EstabelecimentoRetorno)
async def modificar_estabelecimento(id: UUID, estabelecimento: EstabelecimentoEntrada):
    pass


@router_estabelecimentos.delete("/{id}", status_code=204)
async def deletar_estabelecimento(id: UUID):
    pass


@router_estabelecimentos.get("/", response_model=List[EstabelecimentoRetorno])
async def visualizar_estabelecimentos():
    pass


@router_estabelecimentos.get("/{id}", response_model=EstabelecimentoRetorno)
async def visualizar_estabelecimento_por_id(id: UUID):
    pass

from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

from contextos.estabelecimentos.rotas.esquemas import EstabelecimentoDadosBase


class LancamentoRetorno(BaseModel):
    id: UUID
    nome_do_produto: str
    valor_do_produto: float
    estabelecimento_do_lancamento: EstabelecimentoDadosBase
    data_do_lancamento: datetime


class LancamentoEntrada(BaseModel):
    nome_do_produto: str
    valor_do_produto: float
    id_estabelecimento_do_lancamento: UUID
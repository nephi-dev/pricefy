from datetime import datetime
from pydantic import BaseModel

from contextos.estabelecimentos.rotas.esquemas import EstabelecimentoDadosBase


class LancamentoRetorno(BaseModel):
    id: int
    nome_do_produto: str
    valor_do_produto: float
    estabelecimento_do_lancamento: EstabelecimentoDadosBase


class LancamentoEntrada(BaseModel):
    nome_do_produto: str
    valor_do_produto: float
    id_estabelecimento_do_lancamento: int

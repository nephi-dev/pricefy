from pydantic import BaseModel
from uuid import UUID


class EstabelecimentoRetorno(BaseModel):
    id: UUID
    nome: str
    rua: str
    numero: str
    bairro: str
    cep: str
    cidade: str
    estado: str
    telefone: str
    email: str


class EstabelecimentoEntrada(BaseModel):
    nome: str
    rua: str
    numero: str
    bairro: str
    cep: str
    cidade: str
    estado: str
    telefone: str
    email: str


class EstabelecimentoDadosBase(BaseModel):
    id: UUID
    nome: str

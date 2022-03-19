from pydantic import BaseModel


class EstabelecimentoRetorno(BaseModel):
    id: int
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
    id: int
    nome: str

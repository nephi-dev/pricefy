from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextos.estabelecimentos.rotas.api import router_estabelecimentos
from contextos.lancamentos.rotas.api import router_lancamentos

app = FastAPI(
    title="API do Precify",
    description=(
        "Um projeto para unir o preço de diversos"
        " produtos de sua cidade em um só lugar."
    ),
    version="1.0.0",
)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse("/docs")


app.include_router(router_estabelecimentos, prefix="/api/estabelecimentos")
app.include_router(router_lancamentos, prefix="/api/lancamentos")

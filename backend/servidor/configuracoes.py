from fastapi import FastAPI
from fastapi.responses import RedirectResponse

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

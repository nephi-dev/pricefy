import uvicorn

if __name__ == "__main__":
    uvicorn.run("servidor.configuracoes:app", reload=True)

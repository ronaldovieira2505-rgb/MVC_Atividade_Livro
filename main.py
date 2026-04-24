import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from controllers.livro_controller import router as livro_router

app = FastAPI()

# Integrando as rotas do Controller (MVC)
app.include_router(livro_router, prefix="/api")


@app.get("/")
async def read_index():
    # Buscando o caminho exato do arquivo na pasta 'views'
    # Usar o path absoluto evita erros de 'File Not Found' no Windows
    caminho_html = os.path.join(os.getcwd(), "views", "index.html")

    # media_type='text/html' força o navegador a renderizar o código
    return FileResponse(caminho_html, media_type='text/html')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
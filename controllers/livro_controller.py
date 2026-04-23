from fastapi import APIRouter
from models.livro_model import LivroRepository

# Router para organizar as rotas de livros
router = APIRouter()


@router.get("/livros")
def listar_livros():
    """
    Esta função actua como o Controller.
    Ela recebe a requisição GET, pede os dados ao Model e os retorna.
    """
    # O Controller solicita os dados ao Model
    livros = LivroRepository.buscar_todos_os_livros()

    # Retorna os dados que serão exibidos pela View
    return livros
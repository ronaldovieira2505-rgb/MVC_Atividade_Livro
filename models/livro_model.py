
class Livro:
    def __init__(self, id_livro: int, titulo: str, preco: float, sinopse: str):
        self.id = id_livro
        self.titulo = titulo
        self.preco = preco
        self.sinopse = sinopse


# "Banco de Dados" simulado para o MVP
# Em um cenário real, o Model faria a conexão com o banco SQL aqui
_banco_de_dados_livros = [
    Livro(1, "O Senhor dos Anéis", 89.90, "A jornada para destruir o Um Anel."),
    Livro(2, "1984", 45.50, "Grande Irmão está de olho em você."),
    Livro(3, "O Guia do Mochileiro das Galáxias", 39.90, "Não entre em pânico.")
]


class LivroRepository:
    """
    Classe responsável por gerenciar a leitura e escrita no banco de dados[cite: 242].
    Ela abstrai o acesso aos dados para o resto da aplicação.
    """

    @staticmethod
    def buscar_todos_os_livros():
        # Retorna a lista completa do nosso banco de dados simulado
        return _banco_de_dados_livros

    @staticmethod
    def buscar_por_id(id_livro: int):
        # Uma busca simples para encontrar um livro específico
        for livro in _banco_de_dados_livros:
            if livro.id == id_livro:
                return livro
        return None
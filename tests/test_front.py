"""Checagens automáticas das páginas (Aula 11): estrutura e acessibilidade mínima."""
from html.parser import HTMLParser
from pathlib import Path

import pytest

PASTA = Path(__file__).resolve().parent.parent / "front"
PAGINAS = sorted(PASTA.glob("*.html"))


class Leitor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []          # (tag, atributos)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def ler(caminho):
    leitor = Leitor()
    leitor.feed(caminho.read_text(encoding="utf-8"))
    return leitor.tags


@pytest.mark.parametrize("pagina", PAGINAS, ids=lambda p: p.name)
def test_idioma_e_titulo(pagina):
    tags = ler(pagina)
    html = [a for t, a in tags if t == "html"][0]
    assert html.get("lang") == "pt-BR"
    assert any(t == "title" for t, _ in tags)


@pytest.mark.parametrize("pagina", PAGINAS, ids=lambda p: p.name)
def test_estrutura_semantica(pagina):
    nomes = [t for t, _ in ler(pagina)]
    for tag in ("header", "nav", "main", "footer"):
        assert tag in nomes, f"falta <{tag}>"
    assert nomes.count("main") == 1
    assert nomes.count("h1") == 1


@pytest.mark.parametrize("pagina", PAGINAS, ids=lambda p: p.name)
def test_toda_imagem_tem_alt(pagina):
    for tag, atributos in ler(pagina):
        if tag == "img":
            assert "alt" in atributos, f"imagem sem alt: {atributos.get('src')}"


def test_todo_campo_tem_label():
    tags = ler(PASTA / "cadastro.html")
    rotulos = {a.get("for") for t, a in tags if t == "label"}
    for tag, atributos in tags:
        if tag in ("input", "select"):
            assert atributos.get("id") in rotulos, f"campo sem label: {atributos.get('id')}"


def test_campos_do_formulario_batem_com_a_api():
    nomes = {a.get("name") for t, a in ler(PASTA / "cadastro.html") if t in ("input", "select")}
    assert nomes == {"tipo", "nome", "preco", "tamanho"}

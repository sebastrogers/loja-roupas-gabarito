# Loja de Roupas

Projeto construído passo a passo na aula de Coding (Faculdade Senac Pernambuco, 2026.2).

## Como rodar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
fastapi dev api.py              # abre a API em http://127.0.0.1:8000/docs
                                 # os produtos ficam gravados em loja.db
                                 # os produtos ficam gravados em loja.db
```

![testes](https://github.com/SEU-USUARIO/loja-roupas/actions/workflows/testes.yml/badge.svg)

## O que tem aqui

| Pasta ou arquivo | O que é | Aula |
|---|---|---|
| `vitrine.py` | os dados da loja em listas e dicionários | 3 |
| `loja/calculos.py` | total do carrinho e frete, com testes | 4 |
| `loja/produto.py` | Produto, Camiseta e Calça | 6 e 7 |
| `loja/carrinho.py` | o Carrinho, que tem produtos e uma promoção | 6 e 7 |
| `loja/promocao.py` | o contrato Promocao e três promoções | 7 e 8 |
| `.github/workflows/testes.yml` | o GitHub roda os testes a cada push | 8 |
| `api.py` | a loja como API: vitrine, filtro, carrinho e total | 9 |
| `tests/test_api.py` | testes da API com TestClient | 9 |
| `exemplos/sqlite_puro.py` | SQL à mão com o sqlite3 do Python | 10 |
| `loja/banco.py` | a tabela produto e a conexão com o SQLite | 10 |
| `loja/repositorio.py` | o repositório: única parte que conversa com o banco | 10 |
| `loja/servico.py` | as regras do catálogo e as exceções do domínio | 10 |
| `tests/test_repositorio.py`, `tests/test_servico.py` | testes com banco em memória | 10 |
| `front/index.html` | a vitrine, em HTML semântico | 11 |
| `front/cadastro.html` | o formulário de cadastro, acessível | 11 |
| `front/estilo.css` | o visual: Flexbox, Grid e telas pequenas | 11 |
| `tests/test_front.py` | checagens de estrutura e acessibilidade das páginas | 11 |

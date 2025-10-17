# fastapi_dados_mockados

Projeto simples em FastAPI que gera dados de vendas mockados usando a biblioteca
Faker e expõe endpoints para gerar e salvar esses dados em CSV. Ótimo para testes,
provas de conceito e para povoar ambientes de desenvolvimento com dados realistas.

## Estrutura principal

- `main.py` — aplicação FastAPI que implementa o gerador de vendas (`/gerador_vendas`).
- `data_output/` — diretório onde o CSV gerado é salvo (`sales_data.csv`).
- `test_spark.py` — arquivo de exemplo (pode ser removido se não for usado).
- `pyproject.toml` — dependências do projeto (Poetry).

> Observação: o projeto gera dados com a biblioteca `Faker` (pt_BR). Não é
> necessário PySpark para o funcionamento padrão da API.

## Pré-requisitos

- Python 3.12+
- Poetry (recomendado) para instalar dependências

As dependências estão declaradas em `pyproject.toml` (por exemplo: `fastapi`,
`uvicorn`, `faker`, `pandas`, etc.).

## Instalação

1. Instale o Poetry: https://python-poetry.org/
2. No diretório do projeto, instale dependências:

```bash
poetry install
```

3. (Opcional) Entre no shell do Poetry:

```bash
poetry shell
```

## Executando a API

Inicie o servidor Uvicorn apontando para o módulo `main`:

```bash
uvicorn main:app --reload --port 8000
```

## Endpoints principais

- GET /  — rota de saúde (ex.: retorna {"status": "api funfando"}).
- GET /gerador_vendas?records={n} — gera `n` registros (padrão: 10) e grava um CSV
	em `data_output/sales_data.csv`.

Parâmetros da rota `/gerador_vendas`:
- `records` (opcional, int): quantidade de registros a gerar. Exemplo:

```bash
curl "http://127.0.0.1:8000/gerador_vendas?records=25"
```

Resposta (exemplo): JSON com mensagem, quantidade de registros e caminho do CSV.

## Formato do CSV gerado

O CSV `data_output/sales_data.csv` contém as colunas:

- `id_venda` — identificador sequencial
- `plataforma` — exemplo: Mercado Livre, Shopee, Amazon, Magalu, etc.
- `valor_venda` — valor (float)
- `data_venda` — data em formato ISO (YYYY-MM-DD)
- `status` — Pago, Pendente, Cancelado, Reembolsado

## Exemplo: ler o CSV com pandas

```python
import pandas as pd
df = pd.read_csv('data_output/sales_data.csv')
print(df.head())
```

## Observações

- Se `data_output/` não existir, a API criará o diretório ao gerar o CSV.
- O gerador de dados usa `Faker('pt_BR')` para criar datas e dados locais.
- Se houver arquivos de exemplo que você não utiliza (ex.: `test_spark.py`),
	considere removê-los para manter o repositório enxuto.

## Próximos passos (sugestões)

- Adicionar endpoint opcional que retorne os dados gerados em JSON sem
	necessariamente escrever o CSV.
- Adicionar parâmetros para controlar faixa de datas, lista de plataformas e
	status possíveis pela query string.
- Implementar testes automáticos com `pytest` para garantir o formato do CSV
	e o comportamento do endpoint.

---

Se quiser, eu crio um pequeno script em `examples/` que chama o endpoint e
imprime as primeiras linhas usando `requests` + `pandas`. Diga se prefere isso
que eu já adiciono.

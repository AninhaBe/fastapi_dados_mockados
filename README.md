# API de geração de vendas mockadas com FastAPI

Este projeto fornece uma API simples construída com [FastAPI](https://fastapi.tiangolo.com/) para gerar arquivos CSV com vendas fictícias utilizando a biblioteca [Faker](https://faker.readthedocs.io/). O objetivo é acelerar provas de conceito, demonstrações ou testes que precisem de dados tabulares com aparência realista sem depender de bases externas.

A rota principal `/gerador_vendas` cria (ou sobrescreve) `data_output/sales_data.csv` com a quantidade de registros solicitada e retorna uma resposta JSON confirmando o caminho do arquivo.

## Conteúdo

1. [Tecnologias utilizadas](#tecnologias-utilizadas)
2. [Estrutura do projeto](#estrutura-do-projeto)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Executando a API](#executando-a-api)
6. [Endpoints](#endpoints)
7. [Formato dos dados](#formato-dos-dados)
8. [Arquivos auxiliares](#arquivos-auxiliares)
9. [Personalização](#personalização)
10. [Próximos passos sugeridos](#próximos-passos-sugeridos)

## Tecnologias utilizadas

- Python 3.12+
- FastAPI com documentação automática (Swagger UI / ReDoc)
- Uvicorn para executar a aplicação ASGI
- Faker com localidade `pt_BR` para gerar datas realistas
- Poetry para gerenciamento de dependências (recomendado)

> O arquivo `pyproject.toml` lista dependências adicionais como `pandas`, `numpy`, `pyspark` e `dbldatagen`. Elas são úteis para cenários de engenharia de dados, mas não são obrigatórias para executar esta API específica.

## Estrutura do projeto

```text
├── main.py         # Aplicação FastAPI com as rotas e a geração do CSV
├── data_output/    # Pasta onde os arquivos gerados são salvos
├── test_api.py     # Script exemplo de consumo (precisa de ajustes de URL)
├── pyproject.toml  # Definição de dependências via Poetry
└── README.md       # Documentação do projeto
```

O diretório `data_output/` já contém um CSV e um arquivo Parquet de exemplo. Ao gerar novos dados, o CSV é sobrescrito automaticamente.

## Pré-requisitos

- Python 3.12 ou superior instalado.
- [Poetry](https://python-poetry.org/docs/#installation) (opcional, mas recomendado).
- Ferramentas para testar requisições HTTP, como `curl`, `HTTPie` ou até mesmo o navegador via Swagger UI.

## Instalação

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone https://github.com/<sua-conta>/fastapi_dados_mockados.git
   cd fastapi_dados_mockados
   ```
2. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```
3. (Opcional) Ative o ambiente virtual do Poetry:
   ```bash
   poetry shell
   ```

Se preferir usar `pip`, gere um arquivo de requisitos com `poetry export --without-hashes -f requirements.txt > requirements.txt` e instale com `pip install -r requirements.txt`.

## Executando a API

Inicie o servidor com Uvicorn apontando para o módulo `main`:

```bash
uvicorn main:app --reload --port 8000
```

- `--reload` reinicia o servidor automaticamente durante o desenvolvimento.
- Ajuste a porta conforme necessário.

Com o servidor em execução, acesse `http://127.0.0.1:8000/docs` para utilizar a documentação interativa gerada automaticamente pelo FastAPI.

## Endpoints

| Método | Rota             | Descrição                                                                    |
|--------|------------------|-------------------------------------------------------------------------------|
| GET    | `/`              | Verifica se a API está funcionando, retornando `{ "status": "api funfando" }`. |
| GET    | `/gerador_vendas` | Gera o arquivo CSV com vendas simuladas. Aceita o parâmetro de query `records` (padrão 10). |

Exemplo de chamada:

```bash
curl "http://127.0.0.1:8000/gerador_vendas?records=25"
```

Resposta típica:

```json
{
  "message": "Dados gerados com sucesso",
  "records": 25,
  "csv_path": "data_output/sales_data.csv"
}
```

## Formato dos dados

Os dados são salvos com codificação UTF-8 e possuem as seguintes colunas:

| Coluna        | Descrição                                                                 | Exemplo             |
|---------------|---------------------------------------------------------------------------|---------------------|
| `id_venda`    | Identificador sequencial iniciando em 1.                                   | `17`                |
| `plataforma`  | Marketplace aleatório (Mercado Livre, Shopee, Amazon, Magalu etc.).       | `"Shopee"`         |
| `valor_venda` | Valor monetário entre R$ 10,00 e R$ 500,00 com duas casas decimais.       | `354.90`            |
| `data_venda`  | Data no intervalo de 01/01/2025 a 31/12/2025, em formato ISO (`YYYY-MM-DD`). | `"2025-04-15"`     |
| `status`      | Situação da venda (Pago, Pendente, Cancelado ou Reembolsado).             | `"Pago"`           |

A data é gerada como objeto `datetime.date` e convertida para string com `isoformat()` antes de ser escrita no CSV.

## Arquivos auxiliares

- `data_output/sales_data.csv`: arquivo principal gerado pela rota.
- `data_output/sales_data.parquet`: exemplo de saída em Parquet (não é atualizado automaticamente).
- `test_api.py`: script simples usando `requests`. Ele aponta para `http://127.0.0.1:8000/generate_sales`; ajuste a URL para `http://127.0.0.1:8000/gerador_vendas` e adapte as chaves do JSON (`message`, `records`, `csv_path`) caso queira utilizá-lo com esta API.


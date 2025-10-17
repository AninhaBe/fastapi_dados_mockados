from fastapi import FastAPI
from faker import Faker
import random
import csv
import os
import datetime

app = FastAPI(title="Mock API com Faker")

fake = Faker("pt_BR")

@app.get("/")
def root():
    return {"status": "api funfando"}

@app.get("/gerador_vendas")
def gerar_vendas(records: int = 10):
    try:
        output_dir = "data_output"
        os.makedirs(output_dir, exist_ok=True)
        csv_path = os.path.join(output_dir, "sales_data.csv")

        plataformas = ["Mercado Livre", "Shopee", "Amazon", "Magalu", "Tiktok Shop", "Shein"]
        status = ["Pago", "Pendente", "Cancelado", "Reembolsado"]

        # converte explicitamente para objetos datetime.date
        data_inicial = datetime.date.fromisoformat("2025-01-01")
        data_final = datetime.date.fromisoformat("2025-12-31")

        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id_venda", "plataforma", "valor_venda", "data_venda", "status"])

            for i in range(1, records + 1):
                data_venda = fake.date_between(start_date=data_inicial, end_date=data_final)
                writer.writerow([
                    i,
                    random.choice(plataformas),
                    round(random.uniform(10.0, 500.0), 2),
                    data_venda.isoformat(),
                    random.choice(status)
                ])

        return {
            "message": "Dados gerados com sucesso",
            "records": records,
            "csv_path": csv_path
        }

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return {"erro": str(e)}

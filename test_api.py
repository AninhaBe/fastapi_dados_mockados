import requests

url = "http://127.0.0.1:8001/generate_sales?records=35"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Registros gerados: {data['registros']}")
    print("Exemplo de dados:")
    for linha in data["dados"][:3]:
        print(linha)
else:
    print("Erro:", response.status_code, response.text)

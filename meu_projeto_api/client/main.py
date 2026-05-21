import requests

API_URL = "http://127.0.0.1:8000"

def testar_conexao():
    try:
        response = requests.get(f"{API_URL}/")
        print("GET / :", response.json())
    except requests.exceptions.ConnectionError:
        print("Erro de conexao.")

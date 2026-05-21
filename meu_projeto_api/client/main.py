import requests

API_URL = "http://127.0.0.1:8000"

def testar_conexao():
    try:
        response = requests.get(f"{API_URL}/")
        print("GET / :", response.json())
    except requests.exceptions.ConnectionError:
        print("Erro de conexao.")

def enviar_texto_para_ia(texto_usuario):
    payload = {"texto": texto_usuario}
    try:
        response = requests.post(f"{API_URL}/analisar", json=payload)
        if response.status_code == 200:
            print("POST /analisar :", response.json())
    except requests.exceptions.ConnectionError:
        print("Erro de conexao.")

if __name__ == "__main__":
    testar_conexao()
    enviar_texto_para_ia("O projeto esta excelente")
    enviar_texto_para_ia("Deu erro no sistema")
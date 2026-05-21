# Terceiro Mini Projeto
Tema: Consumo de APIs

Projeto desenvolvido para a Fatec Rio Claro. O objetivo é implementar um servidor de APIs e um cliente que consuma dados dessa API.As APIs permitem que sistemas distintos se comuniquem de forma padronizada, sendo possível acessar modelos simulados sem precisar reconstruir a infraestrutura. 

## Execução
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor (na pasta server): `uvicorn app.main:app --reload`
3. Inicie o cliente (na pasta client): `python main.py`
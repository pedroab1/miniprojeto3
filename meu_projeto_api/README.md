# Terceiro Mini Projeto
Tema: Consumo de APIs

Projeto desenvolvido para a Fatec Rio Claro. O objetivo é implementar um servidor de APIs e um cliente que consuma dados dessa API[cite: 7]. [cite_start]As APIs permitem que sistemas distintos se comuniquem de forma padronizada [cite: 5][cite_start], sendo possível acessar modelos simulados sem precisar reconstruir a infraestrutura[cite: 6]. 

## Execução
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor (na pasta server): `uvicorn app.main:app --reload`
3. Inicie o cliente (na pasta client): `python main.py`
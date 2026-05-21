from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AnaliseTexto(BaseModel):
    texto: str

@app.get("/")
def endpoint_raiz():
    return {"status": "online"}

@app.post("/analisar")
def analisar_sentimento(dados: AnaliseTexto):
    texto_minusculo = dados.texto.lower()
    
    if any(palavra in texto_minusculo for palavra in ["bom", "otimo", "excelente"]):
        sentimento = "Positivo"
        confianca = 0.95
    elif any(palavra in texto_minusculo for palavra in ["ruim", "pessimo", "erro"]):
        sentimento = "Negativo"
        confianca = 0.88
    else:
        sentimento = "Neutro"
        confianca = 0.50

    return {
        "texto_analisado": dados.texto,
        "sentimento_predito": sentimento,
        "grau_de_confianca": confianca
    }
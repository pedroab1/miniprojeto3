from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AnaliseTexto(BaseModel):
    texto: str

@app.get("/")
def endpoint_raiz():
    return {"status": "online"}
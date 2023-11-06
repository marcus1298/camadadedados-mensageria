from fastapi import FastAPI
from pydantic import BaseModel
from main import app
import pika
import json

app = FastAPI()

# Configurações do RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='dados_queue')

class Dados(BaseModel):
    nome: str
    matricula: str
    curso: str

@app.post("/enviar_dados")
async def enviar_dados(dados: Dados):
    # Transforma os dados em formato JSON
    dados_json = dados.json()
    
    # Envia os dados para a fila no RabbitMQ
    channel.basic_publish(exchange='', routing_key='dados_queue', body=dados_json)

    return {"status": "Dados enviados com sucesso!"}

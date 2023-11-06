import pika
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configurações do RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='dados_queue')

# Configurações do banco de dados
engine = create_engine('sqlite:///dados.db')
Base = declarative_base()

class Dados(Base):
    __tablename__ = 'dados'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    matricula = Column(String)
    curso = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def callback(ch, method, properties, body):
    # Converte a mensagem JSON para um dicionário
    dados_dict = json.loads(body)

    # Cria um objeto Dados e o adiciona ao banco de dados
    dados_obj = Dados(**dados_dict)
    session.add(dados_obj)
    session.commit()

channel.basic_consume(queue='dados_queue', on_message_callback=callback, auto_ack=True)
print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()

# camadadedados-mensageria
Passos para Testar o Sistema:
Iniciar o RabbitMQ:

Certifique-se de que o RabbitMQ esteja em execução. Se você ainda não o fez, use o seguinte comando:
bash

docker run -d --hostname rabbit --name rabbit13 -p 15672:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
Isso iniciará um contêiner Docker com o RabbitMQ e fornecerá uma interface de gerenciamento em http://localhost:15672 (usuário: guest, senha: guest).

Configurar o Ambiente Virtual:

Certifique-se de estar no diretório do seu projeto e que o ambiente virtual esteja ativado:
bash

cd meu_projeto
source venv/bin/activate  # ou "venv\Scripts\activate" no Windows
Executar o Microserviço FastAPI:

No diretório backend, execute o microserviço FastAPI:
bash

cd backend
uvicorn main:app --reload
O microserviço FastAPI estará disponível em http://127.0.0.1:8000. Acesse a documentação da API em http://127.0.0.1:8000/docs para testar o endpoint /enviar_dados.

Enviar Dados via FastAPI:

Utilize a documentação da API para enviar dados. Preencha os campos nome, matricula, e curso e clique em "Execute". Isso enviará os dados para o RabbitMQ.
Executar o Subscriber para Armazenar no Banco de Dados:

Em um novo terminal, no diretório backend, execute o script do subscriber:
bash

python document_sub.py
Este script estará escutando as mensagens do RabbitMQ e armazenando-as no banco de dados.

Observar a Execução:

Observe os logs do terminal onde você iniciou o uvicorn main:app --reload. Você deve ver mensagens indicando que as requisições estão sendo recebidas.

No terminal onde você executou o python document_sub.py, observe os logs indicando que as mensagens estão sendo recebidas e armazenadas no banco de dados.

Verificar o Banco de Dados:

Verifique se os dados foram armazenados no banco de dados. Dependendo do banco que você está utilizando, você pode usar ferramentas como SQLite Browser para visualizar o arquivo dados.db.

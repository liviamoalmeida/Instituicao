from flask import Flask

# Criar a instância do aplicativo Flask
app = Flask(__name__)

# Importa as rotas depois de configurar o app
from app import routes

from app import app
from flask import render_template

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Outra rota para uma página de exemplo
@app.route('/about')
def about():
    return "Página About"

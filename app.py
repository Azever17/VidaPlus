import os
import sys

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from app.routes import init_routes

app = Flask(__name__)
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True) 
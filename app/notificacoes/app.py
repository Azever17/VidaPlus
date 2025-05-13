from flask import Flask
from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def index():
    return "API de Notificações ativa!"

if __name__ == '__main__':
    app.run(debug=True)

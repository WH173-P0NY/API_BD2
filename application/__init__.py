import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS

# Inicjalizacja SQLAlchemy
db = SQLAlchemy()


def create_app():
    # Ładowanie zmiennych środowiskowych
    load_dotenv()

    # Tworzenie instancji Flask
    app = Flask(__name__)

    # Konfiguracja aplikacji z zmiennych środowiskowych
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .views import api
    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api')
    CORS(app)
    return app
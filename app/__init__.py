from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import Blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        from .routes import main, songs, ranking, auth
        app.register_blueprint(main)
        app.register_blueprint(songs)
        app.register_blueprint(ranking)
        app.register_blueprint(auth)

    return app
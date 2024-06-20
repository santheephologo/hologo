from flask import Flask
from .controllers.convo_controller import convo_blueprint 
from .config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(convo_blueprint)
    app.config.from_object(Config)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    Bootstrap5(app)
    db.init_app(app)

    from marvel.views import marvel
    app.register_blueprint(marvel, url_prefix="/marvel")

    return app

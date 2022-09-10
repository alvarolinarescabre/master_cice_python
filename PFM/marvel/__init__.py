from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SECRET_KEY'] = "6ba7b811-9dad-11d1-80b4-00c04fd430c8'" # Generate by uuid.NAMESPACE_URL
    Bootstrap5(app)
    db.init_app(app)

    from marvel.views import marvel
    app.register_blueprint(marvel, url_prefix="/marvel")

    return app

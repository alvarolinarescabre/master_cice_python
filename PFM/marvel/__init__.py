from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from config import config

db = SQLAlchemy()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SECRET_KEY'] = "6ba7b811-9dad-11d1-80b4-00c04fd430c8'" # Generate by uuid.NAMESPACE_URL
    app.register_error_handler(404, page_not_found)
    Bootstrap5(app)
    db.init_app(app)

    from marvel.views import marvel
    app.register_blueprint(marvel, url_prefix="/")

    return app

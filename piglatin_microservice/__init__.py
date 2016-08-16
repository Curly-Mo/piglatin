#! ../env/bin/python

from flask import Flask

from piglatin_microservice.views.main import main


def create_app(object_name):
    """
    A flask application factory
    """
    app = Flask(__name__)
    app.config.from_object(object_name)


    # register our blueprints
    app.register_blueprint(main)

    return app

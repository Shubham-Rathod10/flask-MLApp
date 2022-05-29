from flask import Flask
from pymongo import MongoClient
from importlib import import_module
from os import path


def create_app(config_filename):
    app = Flask(__name__)
    app.app_context().push()

    @app.after_request
    def add_header(response):
        # response.cache_control.no_store = True
        if 'Cache-Control' not in response.headers:
            response.headers['Cache-Control'] = 'no-store'
        return response

    app.config.from_object(config_filename)
    app.config['BASE_PATH'] = path.dirname(app.instance_path)
    app.config['MONGO_URI'] = app.config['MONGODB_URI']
    app.config['mongo'] = init_db(app.config['MONGO_URI'])
    for module_name in app.config['ENABLE_MODULES']:
        import_module("app." + module_name).init_app(app)
    return app
def init_db(config):
    return MongoClient(config)
from flask.blueprints import Blueprint as APIBlueprint
from app.ImageNet.controller import ImageNetController


def setup_routing(app):
    In1 = APIBlueprint('ImageNet', __name__, subdomain='', url_prefix='')
    In1.route('/imageNet/form', methods=['GET', 'POST'])(ImageNetController().upload_image)
    In1.route('/imageNet/classify', methods=['GET', 'POST'])(ImageNetController().retrieve_classification)
    app.register_blueprint(In1)
    return app
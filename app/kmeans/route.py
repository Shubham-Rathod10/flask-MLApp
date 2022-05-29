from flask.blueprints import Blueprint as APIBlueprint
from app.kmeans.controller import kmeans, home, _algo# kmeansfile

def setup_routing(app):
    km1 = APIBlueprint('KMeans', __name__, subdomain='', url_prefix='')
    km1.route('/', methods=['GET', 'POST'])(home)
    km1.route('/kmeans', methods=['GET', 'POST'])(kmeans)
    #km1.route('/kmeans/file', methods=['GET', 'POST'])(kmeansfile)
    km1.route('/kmeans/output', methods=['GET', 'POST'])(_algo)
    app.register_blueprint(km1)
    return app
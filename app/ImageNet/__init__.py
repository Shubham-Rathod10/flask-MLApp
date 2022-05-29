def init_app(app):
    from app.ImageNet.route import setup_routing as sr
    # route setup
    sr(app)

    return app
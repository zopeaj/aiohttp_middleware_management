from backend.app.api import routes


def setup_routes(app):
    app.add_routes(routes)


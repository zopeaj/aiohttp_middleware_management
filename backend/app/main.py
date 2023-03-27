from aiohttp import web
from app.middleware import error_middleware
from app.routes import setup_routes

app = web.Application(middleware=[error_middleware])
setup_routes(app)

web.run_app(app, host="1270.0.1", port=8081)

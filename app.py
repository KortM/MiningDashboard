from aiohttp import web
from routes import setup_routes, setup_static_routes,UserPolicy, setup_security
import aiohttp_jinja2
import jinja2
import pathlib
from aiohttp_session import SimpleCookieStorage, session_middleware
from aiohttp_security import SessionIdentityPolicy



middleware = session_middleware(SimpleCookieStorage())
policy = SessionIdentityPolicy()

app = web.Application(middlewares=[middleware])
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str('templates')))
setup_routes(app)
setup_static_routes(app)
setup_security(app, policy, UserPolicy())
web.run_app(app)
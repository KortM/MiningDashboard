from aiohttp import web
from routes import setup_routes, setup_static_routes
import aiohttp_jinja2
import jinja2
import pathlib
from aiohttp_session import SimpleCookieStorage, session_middleware
from aiohttp_security import SessionIdentityPolicy




app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str('templates')))
setup_routes(app)
setup_static_routes(app)
web.run_app(app)
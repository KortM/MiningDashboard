from aiohttp import web
import aiohttp_jinja2
from init_db import Hosts, Logs, Session

@aiohttp_jinja2.template('mining.html')
async def index(request):
    s = Session()
    result = s.query(Hosts).all()
    return {'hosts': result}
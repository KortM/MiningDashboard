from aiohttp import web
import aiohttp_jinja2
from init_db import Hosts, Logs, Session

@aiohttp_jinja2.template('mining.html')
async def index(request):
    s = Session()
    up = []
    down = []
    los = []
    result = s.query(Hosts).all()
    [up.append(i) for i in result if i.host_status == 'U']
    [down.append(i) for i in result if i.host_status == 'D']
    [los.append(i) for i in result if i.host_status == 'L']

    return {
        'hosts': result, 
        'UP': len(up),
        'Down': len(down),
        'Los': len(los)
        }
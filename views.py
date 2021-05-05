from aiohttp import web
import aiohttp_jinja2
from init_db import Hosts, Logs, Session


@aiohttp_jinja2.template('posts_preview.html')
async def index(request):
    return {
        "page_name":"Публикации",
        "title": "Главная: Публикации"
    }
    
@aiohttp_jinja2.template('mining.html')
async def dash(request):
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
        'Los': len(los),
        "page_name": "Mining"
        }
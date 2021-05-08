from aiohttp import web
import aiohttp_jinja2
from init_db import Hosts, Logs, Session
from init_db import User, Session
import re

@aiohttp_jinja2.template('posts_preview.html')
async def index(request):
    return {
        "page_name":"Публикации",
        "title": "Главная: Публикации"
    }

@aiohttp_jinja2.template('sign.html')
async def signin(request):
    return None

async def reg(request):
    '''
        Codes: 
            Fail: -1, user exist,
            Fail: 1, not validate,
    '''
    data = await request.post()
    email_validate = re.findall(r'[\w.-]+@[\w.-]+\.?[\w]+?',data['email'])
    if email_validate and len(data['password']) >=6:
        session = Session()
        if session.query(User).filter_by(email = data['email']).all():
            return web.json_response({'Fail': '-1'})
        else:
            user = User(email=data['email'], login=data['login'])
            user.set_password(data['password'])
            session.add(user)
            session.commit()
            return web.json_response({'redirect': '/'})
    else:
        return web.json_response({'Fail': 1})
        
        

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
from aiohttp import web
from views import index, dash, signin, reg
from auth import handler_root
from aiohttp_security import check_permission, \
    is_anonymous, remember, forget, \
    setup as setup_security, SessionIdentityPolicy
from aiohttp_security.abc import AbstractAuthorizationPolicy
from websocket_handler import websocket_handler

def setup_routes(app):
    #Add route to index page
     app.add_routes([
        web.get('/', index),
        web.get('/signin', signin),
        web.post('/reg', reg),
        web.get('/dash', dash),
        #web.get('/login', handler_auth),
        #web.get('/logout', handler_logout),
        web.get('/ws', websocket_handler)])

def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='static',
                          name='static')


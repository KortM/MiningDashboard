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
    app.router.add_get('/', index)
    app.router.add_get('/sign', signin)
    app.router.add_post('/reg', reg)
    app.router.add_get('/dash', dash)
    app.router.add_get('/ws', websocket_handler)

def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='static',
                          name='static')


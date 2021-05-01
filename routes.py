from aiohttp import web
from views import index
from auth import handler_root
from aiohttp_security import check_permission, \
    is_anonymous, remember, forget, \
    setup as setup_security, SessionIdentityPolicy
from aiohttp_security.abc import AbstractAuthorizationPolicy
from websocket_handler import websocket_handler


class UserPolicy(AbstractAuthorizationPolicy):

    async def authorized_userid(self, identity):
        
        return identity
    
    async def permits(self, identity, permission, context=None):
        return identity == '' and permission in ('auth', )

async def handler_root(request):
    is_logged = not await is_anonymous(request)
    return web.Response(text='''<html><head></head><body>
            Hello, I'm Jack, I'm {logged} logged in.<br /><br />
            <a href="/login">Log me in</a><br />
            <a href="/logout">Log me out</a><br /><br />
            Check my permissions,
            when i'm logged in and logged out.<br />
            <a href="/listen">Can I listen?</a><br />
            <a href="/speak">Can I speak?</a><br />
        </body></html>'''.format(
            logged='' if is_logged else 'NOT',
        ), content_type='text/html')


async def handler_logout(request):
    redirect_response = web.HTTPFound('/')
    await forget(request, redirect_response)
    raise redirect_response

async def handler_auth(request):
    await check_permission(request, 'auth')
    return web.Response(body="I can listen!")

async def setup_security(app, policy, UserPolicy):
    setup_security(app, policy, UserPolicy())

def setup_routes(app):
    #Add route to index page
     app.add_routes([
        web.get('/', index),
        web.get('/login', handler_auth),
        web.get('/logout', handler_logout),
        web.get('/ws', websocket_handler)])

def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='static',
                          name='static')


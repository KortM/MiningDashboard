from views import index

def setup_routes(app):
    #Add route to index page
     app.router.add_get('/', index)

def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='static',
                          name='static')
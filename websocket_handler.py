import asyncio
from aiohttp import web, WSMsgType

async def websocket_handler(request):
    
    ws = web.WebSocketResponse()
    print('Await new connection')
    await ws.prepare(request)

    async for msg in ws:
        print(msg)
        if msg.type == WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())
        
        print('websocket connection closed')
        return ws
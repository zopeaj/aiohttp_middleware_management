from aiohttp.web import RouteTableDef

routes = RouteTableDef()

@routes.get('/get')
async def handle_get(request):
    return {  }

@routes.post('/post')
async def handle_post(request):
    pass


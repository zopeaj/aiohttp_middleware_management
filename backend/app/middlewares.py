from aiohttp.web import middleware, json_response, HTTPException

@middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 400:
            return response
        message = response.message
    except HTTPException as ext:
        if ext.status != 404:
            raise
        message = ext.reason
    return json_response({'error': message})


async def route_middleware(overrides):
    pass


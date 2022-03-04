from aiohttp import web
import aiohttp_cors
import click

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)




#-------------------------------------
#       Define port
#-------------------------------------
def port():
    return 9001
#-------------------------------------
#       Create the webserver app
#-------------------------------------
def create_app():
    app = web.Application()
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*":aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*"
            )
        },
    )

    async def status(_):
        return web.Response(text="Webserver running")

    async def version(_):
        return web.Response(text="v0.0.1")

    status_resource = cors.add(app.router.add_resource("/status"))
    cors.add(status_resource.add_route("GET",status))

    status_resource = cors.add(app.router.add_resource("/version"))
    cors.add(status_resource.add_route("GET", version))

    #app.add_routes([web.get('/', handle),
    #                web.get('/{name}', handle)])

    return app

@click.command()
def main():
    return web.run_app(create_app(),port=port(),handle_signals=False)

if __name__ == '__main__':
    main(prog_name="TEST")
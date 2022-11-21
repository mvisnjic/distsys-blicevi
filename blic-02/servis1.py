import aiohttp
import asyncio
from aiohttp import web
import json

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def get_fact(req):
    jokes = []
    users = []
    async with aiohttp.ClientSession() as session:
        for _ in range(6):
            for _ in range(2):
                jokes.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
                users.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
        
            res = await asyncio.gather(*jokes)
            res2 = await asyncio.gather(*users)
        # print(res)
        # print(res2)
        res = [await x.json() for x in res]
        res2 = [await x.json() for x in res2]
    jokes = [] #res
    users = [] #res2
    async with aiohttp.ClientSession() as session:
        for i in range(len(res)):
            jokes.append(asyncio.create_task(session.post("http://0.0.0.0:8082/filterJoke",json=res[i])))
        res = await asyncio.gather(*jokes) 
        res = [await x.json() for x in res]
        
        
        for i in range(len(res2)):
            users.append(asyncio.create_task(session.post("http://0.0.0.0:8081/filterUser",json=res2[i])))
        res2 = await asyncio.gather(*jokes) 
        res2 = [await x.json() for x in res2]
        
    return web.json_response({"status":"ok", "users":res, "jokes": res2}, status=200)




app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
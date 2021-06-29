import asyncio
import json
import websockets
import blogDataSource
import datasource


async def echo(websocket, path):
    print('connected')
    async for message in websocket:
        message = json.loads(message)
        topic = message['topic']

        if topic == "update_user":
            update_profile(message)

        elif topic == "res_check":
            res = checkUserProfile(message)
            if res:
                await websocket.send('ok')
            else:
                await websocket.send('notok')
        elif topic == "getList":
            temp = []
            temp = send_blogs(message)

            for t in temp:
                loos = '{"fname" : '+'"'+t['name']+'"' +' , "imglink" : '+'"'+t['image']+'"'+', "desc": '+'"'+t['desc']+'"'+'}'
                await websocket.send(loos)
        elif topic == "getProjectList":
            temp = []
            temp = getProjectList(message)

            for t in temp:
                loos = '{"name": '+'"'+t['name']+'"'+', "image": '+'"'+t['image']+'"'+', "desc": '+'"'+t['desc']+'"'+', "url": '+'"'+ t['url']+'"'+'}'
                await websocket.send(loos)




def getProjectList(msg):
    search = msg["search"].lower()
    temp = []

    return blogDataSource.search(search)

    # for row in temp:
    #     emit('/res_check1',)
def update_profile(message):
    print('success socket')
    uname = message['name']
    college = message['college']
    email = message['email']
    gender = message['gender']
    datasource.updateProfile(email, uname, college, gender)

def checkUserProfile(message):
    email = message['email']
    if datasource.sessioncheck(email):
          return True
            #emit('res_check', {'status': "ok"})
    return False
        #emit('res_check', {'status': "notok"})


def send_blogs(message):
    searchkey = message['search']
    print('connected:2')
    return blogDataSource.blog_search(searchkey)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', 443))
asyncio.get_event_loop().run_forever()



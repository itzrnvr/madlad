from websocket import create_connection
from threading import Thread
import json

ws = create_connection("ws://localhost:8000/api/v1/chats/all/ws/89")

alive = True


def read():
    while alive:
        print("Server ", ws.recv())


def write(username, message):
    while alive:
        print(">> ")
        mes = {"username": username, "message": message}
        ws.send(json.dumps(mes))


readThread = Thread(target=read)
writeThread = Thread(target=write)

try:
    readThread.start()
    writeThread.start()
except:
    alive = False

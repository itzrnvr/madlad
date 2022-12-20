from websocket import create_connection
from threading import Thread
import json
from .cThread import StoppableThread
import sys

API = "ws://localhost:8000"
class ChatManager:
    def __init__(self, clientID):
        self.onMes = None
        self.ws = create_connection(API + "/api/v1/chats/all/ws/" + clientID)
        readThread = StoppableThread(target=self.read)
        readThread.start()
        # writeThread = StoppableThread(target=self.write)

    def read(self):
        alive = True
        while alive:
            # try:
            mes = self.ws.recv()
            jsonMes = json.loads(mes)
            if self.onMes is not None:
                self.onMes(jsonMes["pfp"], jsonMes["username"], jsonMes["message"])
            print("Server ", mes)
            # except:
            #     alive = False
            #     print("Exiting read")

    def onMessage(self, fn):
        self.onMes = fn

    def sendMessage(self, pfp, username, message):
        mes = {"pfp": pfp, "username": username, "message": message}
        try:
            self.ws.send(json.dumps(mes))
        except:
            print("Something went wrong bruh")

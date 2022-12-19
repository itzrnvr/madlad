from websocket import create_connection
from threading import Thread
import json
from cThread import StoppableThread
import sys


class ChatManager:
    def __init__(self, clientID):
        self.ws = create_connection("wss://concord-28ll.onrender.com/api/v1/chats/all/ws/" + clientID)
        readThread = StoppableThread(target=self.read)
        readThread.start()
        # writeThread = StoppableThread(target=self.write)

    def read(self):
        while True:
            try:
                print("Server ", self.ws.recv())
            except:
                print("Exiting read")

    def sendMessage(self, username, message):
        mes = {"username": username, "message": message}
        try:
            self.ws.send(json.dumps(mes))
        except:
            print("Something went wrong bruh")

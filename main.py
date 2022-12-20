from client import auth
from client import chat


class madlad:
    def __init__(self):
        pass

    def login(self, username, password):
        return auth.login(username, password)

    def register(self, username, password):
        return auth.register(username, password)

    def uploadPfp(self):
        return auth.uploadPfp()

    def getChatManager(self):
        return chat.ChatManager



# client = madlad()
# response =  client.login("Saurav", "444")
# client.register("Shivam", "123")

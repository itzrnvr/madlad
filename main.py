from client import auth
from client import chat


class Madlad:
    def __init__(self):
        pass

    def login(self, pfp, username, password):
        return auth.login(pfp, username, password)

    def register(self, pfp, username, password):
        return auth.register(pfp, username, password)

    def uploadPfp(self):
        return auth.uploadPfp()

    def getChatManager(self):
        return chat.ChatManager


client = Madlad()
response = client.login("", "Saurav", "444")
client.register("https://i.pinimg.com/236x/cc/50/ca/cc50cada4658669e26f818405cc7016b.jpg", "Shivam", "123")
chatMag = client.getChatManager()("88")
chatMag.sendMessage(
    "https://i.pinimg.com/236x/cc/50/ca/cc50cada4658669e26f818405cc7016b.jpg",
    "Shivam",
    "123"
)

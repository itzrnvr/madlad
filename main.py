from client import auth


class madlad:
    def __init__(self):
        pass

    def login(self, username, password):
        return auth.login(username, password)

    def register(self, username, password):
        return auth.register(username, password)


client = madlad()
response =  client.login("Saurav", "444")
# client.register("Shivam", "123")

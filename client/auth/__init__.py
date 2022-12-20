import requests
from pfpmanager import PfpManager

API = "http://localhost:8000/api/v1/auth/users"
hapi = "https://concord-28ll.onrender.com/api/v1/auth/users"

pfpmanager = PfpManager()

def login(username, password):
    data = {"username": username, "password": password}
    req = requests.post(url=hapi + "/login", json=data)
    print(req.text)
    return req.text


def register(username, password):
    data = {"username": username, "password": password}
    req = requests.post(url=hapi + "/register", json=data)
    print(req.text)
    return req.text


def uploadPfp():
    return pfpmanager.getAndUpload()

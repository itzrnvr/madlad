import requests
from .pfpmanager import PfpManager

API = "http://localhost:8000/api/v1/auth/users"
hapi = "https://concord-28ll.onrender.com/api/v1/auth/users"

pfpmanager = PfpManager()


def login(pfp, username, password):
    data = {"pfp": pfp, "username": username, "password": password}
    req = requests.post(url=API + "/login", json=data)
    print(req.text)
    return req.text


def register(pfp, username, password):
    data = {"pfp": pfp, "username": username, "password": password}
    req = requests.post(url=API + "/register", json=data)
    print(req.text)
    return req.text


def uploadPfp():
    return pfpmanager.getAndUpload()

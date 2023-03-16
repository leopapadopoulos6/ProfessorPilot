from flask import Flask

#imports from api
from backend.api import build_api

app = build_api()

if __name__ == '__main':
    app.run()



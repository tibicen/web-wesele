import bottle
from api import names

app = application = names.app


if __name__ == "__main__":
    bottle.run(host="127.0.0.1", port=8000)

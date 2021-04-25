#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from api import formularz

app = application = formularz.app


if __name__ == "__main__":
    bottle.run(host="127.0.0.1", port=8888)

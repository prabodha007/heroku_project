#!/usr/bin/python

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello World!'

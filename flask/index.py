#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello():
    return 'hello world!'

if __name__ == '__main__':
    app.run('0.0.0.0', 6000, True)
#!/usr/bin/env python3
from bottle import run, route, static_file, response

@route('/')
def home():
    response.set_header('Cache-Control','no-cache, no-store, must-revalidate')
    response.set_header('Pragma','no-cache')
    response.set_header('Expires','0')
    return static_file('index.html', root="./")

@route('<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root="./")

run(reloader=True, host='0.0.0.0')

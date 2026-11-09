from flask import request, send_file

def probe():
    return send_file(request.args['file'])

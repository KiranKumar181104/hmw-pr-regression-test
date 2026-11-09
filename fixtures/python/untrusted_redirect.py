from flask import redirect, request

def probe():
    return redirect(request.args['next'])

from flask import render_template_string, request

def probe():
    return render_template_string(request.args['template'])

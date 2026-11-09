from flask import request

def probe(cursor):
    account = request.args['account']
    return cursor.execute(f"SELECT * FROM accounts WHERE name = '{account}'")

import hashlib

def probe(payload):
    return hashlib.md5(payload).hexdigest()

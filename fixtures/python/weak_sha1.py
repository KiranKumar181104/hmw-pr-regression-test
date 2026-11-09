import hashlib

def probe(payload):
    return hashlib.sha1(payload).hexdigest()

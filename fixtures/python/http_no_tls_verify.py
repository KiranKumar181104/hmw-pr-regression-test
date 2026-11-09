import requests

def probe():
    return requests.get('https://example.invalid', verify=False, timeout=1)

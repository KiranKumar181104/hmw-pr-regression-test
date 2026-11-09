import random

def create_reset_token():
    return ''.join(random.choices('0123456789abcdef', k=24))

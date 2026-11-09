import yaml

def probe(payload):
    return yaml.load(payload, Loader=yaml.Loader)

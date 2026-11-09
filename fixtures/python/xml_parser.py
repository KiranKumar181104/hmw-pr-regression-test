from lxml import etree

def probe(payload):
    parser = etree.XMLParser(resolve_entities=True, no_network=False)
    return etree.fromstring(payload, parser=parser)

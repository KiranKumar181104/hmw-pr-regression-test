import subprocess

def probe(value):
    return subprocess.run('echo ' + value, shell=True)

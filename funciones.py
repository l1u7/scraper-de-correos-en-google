import re

def extraerCorreo(texto):
    match = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", texto)
    return match

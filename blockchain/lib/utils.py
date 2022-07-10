import hashlib

def hash(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
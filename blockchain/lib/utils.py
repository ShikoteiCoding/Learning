import hashlib

def hash(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def hash_entries(lhash: str, rhash: str) -> str:
    """ Hash a double entry. """
    return hash(lhash + rhash)
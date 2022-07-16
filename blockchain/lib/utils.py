import hashlib

def digest(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def digest_double_entries(lhash: str, rhash: str) -> str:
    """ Hash a double entry. """
    return digest(lhash + rhash)
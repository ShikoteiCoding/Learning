import hashlib
from Crypto.Hash import RIPEMD160

def double_hash(value: str) -> str:
    sha256 = hashlib.sha256(value.encode('utf-8')).digest()
    h = RIPEMD160.new()
    h.update(sha256)
    return h.hexdigest()

def digest(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def digest_double_entries(lhash: str, rhash: str) -> str:
    """ Hash a double entry. """
    return digest(lhash + rhash)
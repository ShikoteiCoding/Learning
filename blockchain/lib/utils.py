import hashlib
from Crypto.Hash import RIPEMD160
import base58

def base_58_check(value: str) -> str:
    """ Check encode in base 58. """
    return base58.b58encode(value.encode('utf-8')).decode('utf-8')

def double_hash(value: str) -> str:
    """ Hash sha256 and RIPEND160. """
    sha256 = hashlib.sha256(value.encode('utf-8')).digest()
    h = RIPEMD160.new()
    h.update(sha256)
    return str(h)

def digest(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def digest_double_entries(lhash: str, rhash: str) -> str:
    """ Hash a double entry. """
    return digest(lhash + rhash)
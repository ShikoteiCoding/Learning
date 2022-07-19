import hashlib
from typing import Any
from Crypto.Hash import RIPEMD160
import base58
import inspect

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

def cprint(*kwargs: Any) -> None:
    """ Custom print for faster output. """
    output = ""
    for var in kwargs:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items() #type: ignore
        name = [var_name for var_name, var_val in callers_local_vars if var_val is var][0]
        pretty_name = ' '.join([word.title() for word in name.split("_")])
        output += f"\n{pretty_name}: {var} ({type(var)})\n"
    print(output)
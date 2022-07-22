import hashlib
import inspect

from typing import Any, Callable
from Crypto.Hash import RIPEMD160
from fastecdsa.point import Point

ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def encode_elliptic_point(point: Point) -> str:
    """
    From a Point, encode the key in hexa (str) of 257 bits 
    """
    return "0" + hex(point.x + ((2 if point.y % 2 == 0 else 3) << 256))[2:]

def b58check(prefix_version: str, payload: str) -> str:
	# First 8 characters are the 4 first bytes
	checksum_payload = prefix_version + payload
	checksum = sha256(sha256(checksum_payload))[0:8]

	# Encoding the extended payload (payload + checksum)
	b58 = b58encode(str(checksum_payload) + str(checksum))
	return b58

def b58encode(hex_string: str) -> str:
	""" Return a base58 encoded string from hex string """
	cprint(hex_string)
	num = int(hex_string, 16)
	encode = ""
	base_count = len(ALPHABET)
	while (num > 0) :
		num, res = divmod(num, base_count)
		encode = ALPHABET[res] + encode
	return encode

def b58decode(value: str, prefix: bool=False) -> str:
	""" Decode a Base58 encoded string as an integer and return a hex string """
	if not isinstance(value, str):
		value = value.decode('ascii')
	decimal = 0
	for char in value:
		decimal = decimal * 58 + ALPHABET.index(char)
	return hex(decimal)[2:] if not prefix else hex(decimal)

def hash160(value: str) -> str:
	""" Hash sha256 and RIPEND160. Expect an hex value. """
	return ripemd160(sha256(value))

def digest(value: str) -> str:
    """ Hash a string value. """
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def ripemd160(value: str) -> str:
	""" Return a RIPEMD hash of a hex string. """
	byte_array = bytearray.fromhex(value)
	m = RIPEMD160.new()
	m.update(byte_array)
	return m.hexdigest()

def sha256(value: str) -> str:
	""" Return a sha256 hash of a hex string. """
	byte_array = bytearray.fromhex(value)
	m = hashlib.sha256()
	m.update(byte_array)
	return m.hexdigest()

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
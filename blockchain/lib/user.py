from __future__ import annotations

from dataclasses import dataclass, field

from .utils import digest, double_hash

import fastecdsa.keys
import fastecdsa.curve
import fastecdsa.encoding.sec1
from fastecdsa.point import Point

class NoExistingPrivateKey(Exception):
    ...
class NoExistingKeysPair(Exception):
    ...

CURVE = fastecdsa.curve.secp256k1
DATA_PATH = "data/"
PUBLIC_KEY_FILE_SUFFIX = "-public-key.txt"
PRIVATE_KEY_FILE_SUFFIX = "-private-key.txt"

###########################
#   Functions to encode.  #
###########################

def encode_elliptic_point(public_key: Point) -> str:
    """
    From a Point, encode the key in hexa (str) of 257 bits 
    """
    return hex(public_key.x + ((2 if public_key.y % 2 == 0 else 3) << 256))

def generate_private_key_from_value(value: str) -> int:
    """ 
    Generate a private key from digesting a provided string. 
    Warning: value should be randomly generated under CSPRNG generator standard.
    This is for simplicity only.
    """
    # Value is not really a "str" but an hexadecimal number.
    # Convert it back to decimal.
    return int(digest(value), base=16)

def generate_public_key_from_private_key(private_key: int) -> tuple[Point, str]:
    """ 
    Generate a public key from applying elliptic curve multiplication to the private key.
    """
    # Compute the public key (points in elliptic curve space)
    public_key = fastecdsa.keys.get_public_key(private_key, CURVE)

    # Compress the key (256 + 1 bits)
    return public_key, encode_elliptic_point(public_key)

def generate_address_from_public_key(public_key_encoded: str) -> str:
    """
    Generate an address from a public key. (Point in elliptic curve)
    """
    return double_hash(public_key_encoded)

###########################
#     User base class.    #
###########################

@dataclass
class User:
    name: str = field(init=True)

    __private_key: int = field(init=False)
    __public_key: Point = field(init=False)
    __public_key_encoded: str = field(init=False)
    __address: str = field(init=False)

    @property
    def private_key(self) -> int:
        """ Get the private key of the user """
        return self.__private_key
    
    @private_key.setter
    def private_key(self, value: int) -> None:
        """ Set the private key of the user. """
        self.__private_key = value

    @property
    def public_key(self) -> Point:
        """ Get the public key of the user. """
        return self.__public_key

    @public_key.setter
    def public_key(self, value: Point) -> None:
        """ Set the public key of the user. """
        self.__public_key = value

    @property
    def public_key_encoded(self) -> str:
        """ Get the public key encoded of the user. """
        return self.__public_key_encoded

    @public_key_encoded.setter
    def public_key_encoded(self, value: str) -> None:
        """ Set the public key encoded of the user. """
        self.__public_key_encoded = value

    def set_keys(self, private_key: int, public_key: Point, public_key_encoded: str) -> None:
        """ Set generated keys for user. """
        self.__private_key = private_key
        self.__public_key = public_key
        self.__public_key_encoded = public_key_encoded

    @staticmethod
    def export_(user: User, data_path: str = DATA_PATH) -> None:
        """ Use builtin functions of elliptic curves to export keys. """
        if not user.private_key or not user.public_key:
            raise NoExistingKeysPair("User provided does not have existing private and public key.")

        fastecdsa.keys.export_key(user.public_key, CURVE, data_path + user.name + PUBLIC_KEY_FILE_SUFFIX)
        fastecdsa.keys.export_key(user.private_key, CURVE, data_path + user.name + PRIVATE_KEY_FILE_SUFFIX)

    @staticmethod
    def import_(username: str, data_path: str = DATA_PATH) -> User:
        """ Use builtin functions of elliptic curves to import keys. """

        user = User(username)

        private_key = fastecdsa.keys.import_key(data_path + username + PRIVATE_KEY_FILE_SUFFIX, CURVE)
        public_key = fastecdsa.keys.import_key(data_path + username + PUBLIC_KEY_FILE_SUFFIX, CURVE)
        
        if private_key[0]:
            user.set_keys(private_key[0], public_key[1], encode_elliptic_point(public_key[1]))

        return user
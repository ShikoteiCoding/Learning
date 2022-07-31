from __future__ import annotations

from dataclasses import InitVar, dataclass, field

from blockchain.lib.keys import PrivateKey

from .utils import digest, hash160, b58encode
from .keys import PublicKey, PrivateKey, Address

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
    return b58encode(hash160(public_key_encoded))

###########################
#     User base class.    #
###########################

@dataclass
class User:
    name: str = field(init=True)
    pkey: InitVar[PrivateKey | None]= field(init=True, default=None)

    __private_key: PrivateKey = field(init=False)
    __public_key: PublicKey = field(init=False)
    __address: Address = field(init=False)

    def __post_init__(self, pkey: PrivateKey | None) -> None:
        if pkey:
            self.__private_key = pkey
            self.__public_key, self.__address = User.transform_private_key(pkey)

    @staticmethod
    def transform_private_key(key: PrivateKey) -> tuple[PublicKey, Address]:
        pkey = PublicKey(key)
        return pkey, Address(pkey)

    @property
    def private_key(self) -> PrivateKey:
        """ Get the private key of the user """
        return self.__private_key

    @private_key.setter
    def private_key(self, key: PrivateKey) -> None:
        """ Set the private key. Update the dependencies. """
        self.__private_key = key

    @property
    def public_key(self) -> PublicKey:
        """ Get the public key of the user. """
        return self.__public_key
    
    @property
    def address(self) -> Address:
        """ Get the address of the user. """
        return self.__address

    @staticmethod
    def export_(user: User, data_path: str = DATA_PATH) -> None:
        """ Use builtin functions of elliptic curves to export keys. """
        if not user.private_key:
            raise NoExistingKeysPair("User provided does not have existing private and public key.")

        fastecdsa.keys.export_key(user.private_key, CURVE, data_path + user.name + PRIVATE_KEY_FILE_SUFFIX)

    @staticmethod
    def import_(username: str, data_path: str = DATA_PATH) -> User:
        """ Use builtin functions of elliptic curves to import keys. """
        private_key = fastecdsa.keys.import_key(data_path + username + PRIVATE_KEY_FILE_SUFFIX, CURVE)
        
        user = User(username)
        if private_key[0]:
            user.private_key = PrivateKey(private_key[0])

        return user
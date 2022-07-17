from dataclasses import dataclass, field

from .utils import digest

import fastecdsa.keys
import fastecdsa.curve

class NoExistingPrivateKey(Exception):
    ...

def generate_private_key_from_value(value: str) -> str:
        """ 
        Generate a private key from digesting a provided string. 
        Warning: value should be randomly generated under CSPRNG generator standard.
        This is for simplicity only.
        """
        return digest(value)

def generate_public_key_from_private_key(private_key: str) -> str:
        """ 
        Generate a public key from applying elliptic curve multiplication to the private key.
        """
        # Generate an elliptic curve
        curve = fastecdsa.curve.secp256k1

        # Elliptic curve expect integers to compute intersection points with the curve
        private_key_raw = int(private_key, base=16)

        # Compute the public key (points in elliptic curve space)
        public_key = fastecdsa.keys.get_public_key(private_key_raw, curve)

        # Compress the key (256 + 1 bits)
        compressed_pubkey = public_key.x + ((2 if public_key.y % 2 == 0 else 3) << 256)
        return hex(compressed_pubkey)



@dataclass
class User:
    __private_key: str = field(init=False, default="")
    __public_key: str = field(init=False, default="")

    @property
    def private_key(self) -> str:
        """ Get the private key of the user """
        return self.__private_key
    
    @private_key.setter
    def private_key(self, value: str) -> None:
        """ Set the private key of the user. """
        self.__private_key = value

    @property
    def public_key(self) -> str:
        """ Get the public key of the user. """
        return self.__public_key

    @public_key.setter
    def public_key(self, value: str) -> None:
        """ Set the public key of the user. """
        self.__public_key = value
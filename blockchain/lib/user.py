from __future__ import annotations

from dataclasses import dataclass, field

from .utils import digest

import fastecdsa.keys
import fastecdsa.curve
import fastecdsa.encoding.sec1

class NoExistingPrivateKey(Exception):
    ...
class NoExistingKeysPair(Exception):
    ...

CURVE = fastecdsa.curve.secp256k1

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
        # Elliptic curve expect integers to compute intersection points with the curve
        private_key_raw = int(private_key, base=16)

        # Compute the public key (points in elliptic curve space)
        public_key = fastecdsa.keys.get_public_key(private_key_raw, CURVE)

        # Compress the key (256 + 1 bits)
        compressed_pubkey = public_key.x + ((2 if public_key.y % 2 == 0 else 3) << 256)
        return hex(compressed_pubkey)



@dataclass
class User:
    name: str = field(init=True)                      # for convenience only.
    __private_key: str = field(init=False, default="")  # Use str of int key (base 16 keys)
    __public_key: str = field(init=False, default="")   # 

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

    def set_keys(self, private_key: str, public_key: str) -> None:
        """ Set generated keys for user. """
        self.__private_key = private_key
        self.__public_key = public_key

    @staticmethod
    def export_user(user: User, data_path: str):
        if not user.private_key or not user.public_key:
            raise NoExistingKeysPair("User provided does not have existing private and public key.")

        # Export public key
        with open(data_path + user.name + '-public-key.txt', 'w') as f:
            public_key = fastecdsa.encoding.sec1.SEC1Encoder().decode_public_key(user.public_key, CURVE)
            content = fastecdsa.keys.export_key(public_key, CURVE)
            f.write(content or '')

        # Export private key
        with open(data_path + user.name + '-public-key.txt', 'w') as f:
            private_key_raw = int(user.private_key, base=16)
            content = fastecdsa.keys.export_key(private_key_raw, CURVE)
            f.write(content or '')
from dataclasses import InitVar, dataclass, field
from tabnanny import check
from lib.utils import b58encode, cprint, sha256, encode_elliptic_point

from fastecdsa.point import Point
from fastecdsa.curve import Curve

import fastecdsa.keys
import fastecdsa.curve
import fastecdsa.encoding.sec1

import sys

HEX_PREFIX = "0x"
WIF_PREFIX = "80"
CURVE = fastecdsa.curve.secp256k1

class EncodingNotValid(Exception):
    ...


@dataclass
class PrivateKey:
    """ Define a Private Key with methods to manipulate easier. """

    value: InitVar[int | str]

    # Value of private key is the base 10 integer
    __value: int = field(init=False)

    def __post_init__(self, value: int | str):
        
        str_value: str = str(value)

        if not (type(value) == str or type(value) == int):
            raise EncodingNotValid("Expecting either an integer or a string as an hexadecimal format.")

        if type(value) == str:
            assert str_value.startswith(HEX_PREFIX), f"Expecting either an integer or a hex string starting with {HEX_PREFIX}."
            self.__value = int(str_value, base=16)

        if type(value) == int:
            bit_length: int = int(str_value).bit_length()
            assert bit_length == 256, f"Integer Provided is not 256-bits: {bit_length}-bits"
            self.__value = int(str_value)

    def __str__(self) -> str:
        return str(self.__value)

    def __len__(self) -> int:
        return len(str(self.__value))

    @property
    def decimal_value(self) -> int:
        return self.__value

    @property
    def bit_size(self) -> int:
        return self.__value.bit_length()

    def hex(self, prefix: bool=False) -> str:
        """ Return the Private Key in hexadecimal format. """
        if not prefix: return hex(self.__value)[2:]
        return hex(self.__value)

    def wif(self, compressed: bool=False) -> str:
        """ Return the Private Key in Wallet format. """
        # Remove the hexadecimal prefix
        hex_value = self.hex(prefix=False).upper()
        
        # Create the extended version of the hexadecimal key
        compression = '' if not compressed else '01'
        extended = WIF_PREFIX + hex_value + compression

        # Compute the checksum
        checksum = sha256(sha256(extended.upper()).upper())[0:8]

        extended_checksum = extended + checksum.upper()

        cprint(hex_value, compression, extended, checksum, extended_checksum)
            
        return b58encode(extended_checksum)

@dataclass
class PublicKey():
    """ Define a Public Key with methods to manipulate easier. """

    value: InitVar[PrivateKey]
    curve: InitVar[Curve] = CURVE

    # Value of public key is "Compressed Hexadecimal (with 0x prefix)"
    __value: str = field(init=False)

    def __post_init__(self, value: PrivateKey, curve: Curve):
        
        str_value: str = str(value)

        if type(value) != PrivateKey:
            raise EncodingNotValid("Expecting a PrivateKey.")

        self.__value = encode_elliptic_point(fastecdsa.keys.get_public_key(int(str_value, base=10), curve))

    def __str__(self) -> str:
        return str(self.__value)

@dataclass
class Address():
    """ Define an Address to register a Block or transactions. """

    value: InitVar[PublicKey]
    curve: InitVar[Curve] = CURVE

    __value: str = field(init=False)

    def __post_init__(self, value: PublicKey, curve: Curve) -> None:
        
        str_value: str = str(value)

        
from dataclasses import InitVar, dataclass, field
from tabnanny import check
from lib.utils import b58encode, cprint, sha256, encode_elliptic_point, hash160, b58check

from fastecdsa.point import Point
from fastecdsa.curve import Curve

import fastecdsa.keys
import fastecdsa.curve
import fastecdsa.encoding.sec1

import sys

HEX_PREFIX = "0x"
WIF_PREFIX = "80"
B58_PREFIX = "00"
PUK_PREFIX = "04"
CURVE = fastecdsa.curve.secp256k1

class EncodingNotValid(Exception):
    ...


@dataclass
class PrivateKey:
    """ Define a Private Key with methods to manipulate easier. """

    init_value: InitVar[int | str]

    # Value of private key is the base 10 integer
    __value: int = field(init=False)

    def __post_init__(self, init_value: int | str):
        
        str_value: str = str(init_value)

        assert type(init_value) == str or type(init_value) == int, "Expecting either an integer or a string as an hexadecimal format."

        if type(init_value) == str:
            assert str_value.startswith(HEX_PREFIX), f"Expecting either an integer or a hex string starting with {HEX_PREFIX}."
            self.__value = int(str_value, base=16)

        if type(init_value) == int:
            self.__value = int(init_value)

    def __str__(self) -> str:
        return str(self.__value)

    def __len__(self) -> int:
        return len(str(self.__value))

    @property
    def value(self) -> int:
        return self.__value

    def bit_length(self) -> int:
        return self.__value.bit_length()

    def hex(self, prefixed: bool = False, compressed: bool = False) -> str:
        """ Return the Private Key in hexadecimal format. """
        compression = '' if not compressed else '01'
        digest = hex(self.__value)[0:] if prefixed else hex(self.__value)[2:]
        return digest + compression

    def wif(self, compressed: bool = False) -> str:
        """ Return the Private Key in Wallet format. """
        # Remove the hexadecimal prefix
        hex_value = self.hex(prefixed=False, compressed=False).upper()
        
        # Create the extended version of the hexadecimal key
        compression = '' if not compressed else '01'
            
        return b58check(WIF_PREFIX, hex_value + compression)

@dataclass
class PublicKey():
    """ Define a Public Key with methods to manipulate easier. """

    init_value: InitVar[PrivateKey]
    curve: InitVar[Curve] = CURVE

    # Value of public key is "Compressed Hexadecimal (with 0x prefix)"
    __value: tuple[int, int] = field(init=False)

    def __post_init__(self, value: PrivateKey, curve: Curve):
        
        str_value: str = str(value)

        assert type(value) == PrivateKey, "Expecting a PrivateKey."
        p: Point = fastecdsa.keys.get_public_key(int(str_value, base=10), curve)
        self.__value = (p.x, p.y)

    def __str__(self) -> str:
        return str(self.__value)

    def __len__(self) -> int:
        return len(self.__value)

    @property
    def x(self) -> int:
        return self.__value[0]
    
    @property
    def y(self) -> int:
        return self.__value[1]

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y

    @property
    def value(self) -> str:
        return self.hex()

    def hex(self, prefixed: bool = False, compressed: bool = False) -> str:
        prefix = HEX_PREFIX if prefixed else ""
        if compressed:
            return prefix + encode_elliptic_point(Point(self.x, self.y, CURVE))
        encoding = PUK_PREFIX + str(hex(self.x))[2:] + str(hex(self.y))[2:]
        return prefix + encoding

@dataclass
class Address():
    """ Define an Address to register a Block or transactions. """

    init_value: InitVar[PublicKey]
    compressed: InitVar[bool] = False
    curve: InitVar[Curve] = CURVE

    __value: str = field(init=False)

    def __post_init__(self, value: PublicKey, compressed: bool, curve: Curve) -> None:

        assert type(value) == PublicKey, "Expecting a Public Key."
        
        str_value: str = value.hex(compressed=compressed)

        self.__value = b58check(B58_PREFIX, hash160(str_value))
    
    def __str__(self) -> str:
        return self.__value

    def __len__(self) -> int:
        return len(self.__value)

    @property
    def value(self) -> str:
        return self.__value
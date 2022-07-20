from dataclasses import InitVar, dataclass, field
from tabnanny import check
from lib.utils import b58encode, cprint, sha256

import sys

HEX_PREFIX = "0x"
WIF_PREFIX = "80"

class EncodingNotValid(Exception):
    ...

@dataclass
class PrivateKey:

    value: InitVar[int | str]

    decimal_value: int = field(init=False)

    def __post_init__(self, value: int | str):
        
        str_value: str = str(value)

        if not (type(value) == str or type(value) == int):
            raise EncodingNotValid("Expecting either an integer or a string as an hexadecimal format.")

        if type(value) == str:
            assert str_value.startswith(HEX_PREFIX), f"Expecting either an integer or a hex string starting with {HEX_PREFIX}."
            self.decimal_value = int(str_value, base=16)

        if type(value) == int:
            bit_length: int = int(str_value).bit_length()
            assert bit_length == 256, f"Integer Provided is not 256-bits: {bit_length}-bits"
            self.decimal_value = int(str_value)

    def __str__(self) -> str:
        return str(self.decimal_value)

    def __len__(self) -> int:
        return len(str(self.decimal_value))

    @property
    def bit_size(self) -> int:
        return self.decimal_value.bit_length()

    def hex(self, prefix: bool=False) -> str:
        if not prefix: return hex(self.decimal_value)[2:]
        return hex(self.decimal_value)

    def wif(self, compressed: bool=False) -> str:
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
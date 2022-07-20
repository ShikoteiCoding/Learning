from dataclasses import InitVar, dataclass, field

HEX_PREFIX = "0x"

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
            if str_value.startswith(HEX_PREFIX):
                self.decimal_value = int(str_value, base=16)
            else:
                raise EncodingNotValid(f"Expecting either an integer or a hex string starting with {HEX_PREFIX}.")

        if type(value) == int:
            self.decimal_value = int(str_value)

    def __str__(self) -> str:
        return str(self.decimal_value)

    def __len__(self) -> int:
        return len(str(self.decimal_value))

    def hex(self, prefix=True) -> str:
        if not prefix:
            return hex(self.decimal_value)[2:]
        return hex(self.decimal_value)
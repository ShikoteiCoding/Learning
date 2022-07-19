
class PrivateKey:

    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def hex(self, prefix=True) -> str:
        if not prefix:
            return hex(self.value)[2:]
        return hex(self.value)
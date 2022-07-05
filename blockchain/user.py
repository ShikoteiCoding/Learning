from dataclasses import dataclass, field


def generate_keys() -> tuple[str, str]:
    raise NotImplementedError

@dataclass
class User:
    public_key: str = field(init=False)
    private_key: str = field(init=False)

    def __post_init__(self):
        public_key, private_key = generate_keys()



from dataclasses import dataclass, field
import datetime


@dataclass
class Transaction:
    """
    Network transaction data structure.

    For this simplified example, transaction will be validated before being sent to the server.
    There will be no implementation of peer-to-peer network.
    Transactions are then queuing in the "server" and when time is up, transaction are sent to miners.
    Transactions are then encoded into a mekle tree to constitute a block.

    TODO : Consider hasing the byte version and not the str version.
    """

    version: str = field(default="")
    input_counter: int = field(default=0)
    inputs: list[int] = field(default_factory=list)
    output_counter: int = field(default=0)
    outputs: list[int] = field(default_factory=list)

    def __str__(self):
        return self.version + str(self.input_counter) + str(self.inputs) + str(self.output_counter) + str(self.outputs)
from helper import little_endian_to_int, read_varint
from tx import TxIn, TxOut
from io import BytesIO

class Tx:

    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins  # <1>
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet  # <2>
        
    @classmethod
    def parse(cls, s, testnet=False):
        version = little_endian_to_int(s.read(4))
        num_inputs = read_varint(s)
        inputs = []
        for _ in range(num_inputs):
            inputs.append(TxIn.parse(s))
        num_outputs = read_varint(s)
        outputs = []
        for _ in range(num_outputs):
            outputs.append(TxOut.parse(s))
        locktime = little_endian_to_int(s.read(4))
        return cls(version, inputs, outputs, locktime, testnet=testnet)
    

hex_transaction = "020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000"

stream = BytesIO(bytes.fromhex(hex_transaction))

parsed_transaction = Tx.parse(stream)
print("Parsed Transaction:")
print(f"Version: {parsed_transaction.version}")
print("Inputs:")
for tx_in in parsed_transaction.tx_ins:
    print(f"  {tx_in}")
print("Outputs:")
for tx_out in parsed_transaction.tx_outs:
    print(f"  {tx_out}")
print(f"Locktime: {parsed_transaction.locktime}")
print(f"Testnet: {parsed_transaction.testnet}")


from helper import little_endian_to_int
from script import Script

# class TxIn:

#     def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
#         self.prev_tx = prev_tx
#         self.prev_index = prev_index
#         if script_sig is None:
#             self.script_sig = Script()
#         else:
#             self.script_sig = script_sig
#         self.sequence = sequence

#     def __repr__(self):
#         return '{}:{}'.format(
#             self.prev_tx.hex(),
#             self.prev_index,
#         )

#     @classmethod
#     def parse(cls, s):
#         '''Takes a byte stream and parses the tx_input at the start
#         return a TxIn object
#         '''
#         # prev_tx is 32 bytes, little endian
#         prev_tx = s.read(32)[::-1]
#         # prev_index is an integer in 4 bytes, little endian
#         prev_index = little_endian_to_int(s.read(4))
#         # use Script.parse to get the ScriptSig
#         script_sig = Script.parse(s)
#         # sequence is an integer in 4 bytes, little-endian
#         sequence = little_endian_to_int(s.read(4))
#         # return an instance of the class (see __init__ for args)
#         return cls(prev_tx, prev_index, script_sig, sequence)

# class TxOut:

#     def __init__(self, amount, script_pubkey):
#         self.amount = amount
#         self.script_pubkey = script_pubkey

#     def __repr__(self):
#         return '{}:{}'.format(self.amount, self.script_pubkey)

#     @classmethod
#     def parse(cls, s):
#         '''Takes a byte stream and parses the tx_output at the start
#         return a TxOut object
#         '''
#         # amount is an integer in 8 bytes, little endian
#         amount = little_endian_to_int(s.read(8))
#         # use Script.parse to get the ScriptPubKey
#         script_pubkey = Script.parse(s)
#         # return an instance of the class (see __init__ for args)
#         return cls(amount, script_pubkey)



class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        self.script_sig = script_sig
        self.sequence = sequence

    @classmethod
    def parse(cls, s):
        prev_index = little_endian_to_int(s.read(4))
        previous_output = s.read(32)  
        script_sig_length = little_endian_to_int(s.read(1))
        script_sig = s.read(script_sig_length)
        sequence = little_endian_to_int(s.read(4))

        return TxIn(prev_tx=previous_output,prev_index=prev_index, sequence=sequence, script_sig=script_sig)


class TxOut:

    def __init__(self, value, script_pubkey):
        self.value = value
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return f"TxOut(value={self.value}, script_pubkey={self.script_pubkey.hex()})"
    

    @classmethod
    def parse(cls, s):
        value = little_endian_to_int(s.read(8))  
        script_pubkey_length = little_endian_to_int(s.read(1))
        script_pubkey = s.read(script_pubkey_length)

        return TxOut(value=value, script_pubkey=script_pubkey)
        
        

    
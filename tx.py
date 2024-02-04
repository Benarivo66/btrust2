from helper import little_endian_to_int
# from script import Script

class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
    
    
    

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses the tx_input at the start
        return a TxIn object
        '''
        # prev_tx is 32 bytes, little endian
        # prev_index is an integer in 4 bytes, little endian
        # use Script.parse to get the ScriptSig
        # sequence is an integer in 4 bytes, little-endian
        # return an instance of the class (see __init__ for args)
        
        version = little_endian_to_int(s.read(4))
        previous_output = s.read(32)  
        script_sig_length = little_endian_to_int(s.read(1))
        script_sig = s.read(script_sig_length)
        sequence = little_endian_to_int(s.read(4))

        return TxIn(version=version, sequence=sequence, script_sig=script_sig)



# tag::source3[]
class TxOut:

    def __init__(self, value, script_pubkey):
        self.value = value
        self.script_pubkey = script_pubkey
    
    # Update the TxOut class definition

    def __repr__(self):
        return f"TxOut(value={self.value}, script_pubkey={self.script_pubkey.hex()})"
    

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses the tx_output at the start
        return a TxOut object
        '''
        # amount is an integer in 8 bytes, little endian
        # use Script.parse to get the ScriptPubKey
        # return an instance of the class (see __init__ for args)
        
        value = little_endian_to_int(s.read(8))  
        script_pubkey_length = little_endian_to_int(s.read(1))
        script_pubkey = s.read(script_pubkey_length)

        return TxOut(value=value, script_pubkey=script_pubkey)
        
        # value = little_endian_to_int(s.read(8))
        # script_pubkey = Script.parse(s)
        # return TxOut(value=value, script_pubkey=script_pubkey)


    
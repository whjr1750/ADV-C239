import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
    transaction = {
        'sender': 'Satoshi',
        'recipient': 'Mike',
        'amount': '5 ETH'
    }
    data = {
        'index': 1,
        'timestamp': time(),
        'transactions': transaction,
        'gas/fee': 0.1,
        'proof': proof,
        'previous_hash': previous_hash,
    }
    chain.append(data)
    print("block information:", data)
    string_object = json.dumps(data)
    block_string = string_object.encode()

    raw_hash = hashlib.sha256(block_string)
    hex_hash = raw_hash.hexdigest()
    print("Hash code of block:", hex_hash)


block(previous_hash="No previous Hash. Since this is the first block.", proof=000)
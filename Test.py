import hashlib
import json
from time import time

chain = []

def block(proof,previous_hash=None):
	transaction = {
	    'sender' : 'Jay',
	    'recipient' : 'Yash',
	    'amount' : '5 ETH'
	}
    data = {
        'index' : 1,
        'timestamp' : time(),
        'transactions' : transaction,
        'gas/fee' : 0.1,
        'proof' : proof,
        'previous_hash' : previous_hash
    }
    chain.append(data)
    print("appended data: " , data)
    jscon = json.dumps(data)
    string_object=jscon.encode()
    enc = hashlib.sha256(string_object)
    result = enc.hexdigest()

    print("Encrypted data: " , result)

block(previous_hash='No previous hash as this is the first one',proof=000)
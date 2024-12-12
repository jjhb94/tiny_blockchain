# this is the first block on the chain! Genesis ~
from berjakCoin import Block
import datetime as date

def create_genesis_block():
    # manually create a block with
    # index zero and arbitrary previous hash
    # Block(self, index, timestamp, data, previous_hash)
    return Block(0, date.datetime.now(), "Genesis Block", "0")
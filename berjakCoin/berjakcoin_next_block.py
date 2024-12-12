from berjakCoin import Block
import datetime as date

# take the previous block as parameter, 
# create data for the block to be generated
# return new block with it's data - rinse and repeat
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Woah, I'm in the blockchain now! " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
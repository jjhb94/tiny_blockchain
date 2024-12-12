from berjakCoin import create_genesis_block, next_block

# create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# specifiy # of blocks to add to chain
# after genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for block in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been addeed to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

#print(f"latest local ganache block: {w3.eth.get_block('latest')}")
flag = w3.is_connected()
print(flag)

buyer = '0x6D358E8d8Ebf515B505Ef52bcE224f91e66DF63C'
buyer_key = '0x01aa1247c1c80849c8704f82f7ca9e1a00a4f375c1b325084d19cffa8cf555a4'

seller = '0xad18A1daA22256749c3Ec998c1443b943C9BFA2A'
seller_key='0x34e3d201cdcf345455accc1c9298a0b00a623d848e27a38117b5c21dc4c04628'

flag =  w3.is_address(buyer)
print(flag)
flag = w3.is_checksum_address(seller)
print(flag)
import json

# genesis_block = json.loads(w3.to_JSON(w3.eth.getBlock(0)))
# print(genesis_block)

# Fetch balance
balance_wei = w3.eth.get_balance(buyer)
balance_eth = w3.from_wei(balance_wei, 'ether')
print(balance_wei)
# Create a dictionary to hold the data
data = {
    'address': buyer,
    'balance_wei': balance_wei,
    'balance_eth': float(balance_eth)
}

# Convert dictionary to JSON
json_data = json.dumps(data, indent=4)

# Print JSON data
print(json_data)



# buyer_seller_txn = {
#     'from': buyer,
#     'to': seller,
#     'value': w3.to_wei(1, 'ether'),
#     'gas': 90000,
#     'gasPrice': 18000000000,
#     'nonce': 0,
#     'chainId': 2022
#     }

# signed_txn = w3.eth.account.sign_transaction(buyer_seller_txn, buyer_key)

# txn = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
# print(txn)
# print(w3.eth.blockNumber)
# 
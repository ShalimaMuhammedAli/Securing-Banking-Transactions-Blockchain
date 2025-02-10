from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

#print(f"latest local ganache block: {w3.eth.get_block('latest')}")
flag = w3.is_connected()
print(flag)

buyer = '0x55772b506CA9c817117059846B62ecD4E9E9635f'
buyer_key = '0x4b8068e76a3d26c20f7b4f41b27b0f4e9ecac7cc441953ea25f4a0fa3054feaf'

seller = '0x7f8c6dc74DD2498023Cf64E2B731a9456FeA212B'
seller_key='0xe0fefdd54277a63ec2cb758f6d8457e6d302f1b1fc74334613c7344db4f5eb13'

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
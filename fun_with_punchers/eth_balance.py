from web3 import Web3

print("import complete")

# connect to the Ethereum client
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
print("connection complete")

# address of the wallet to query
wallet_address = '0xd1A4D803777db60Ba9bb09692EdF6940cAe77cdF'

# get the balance in wei
balance = web3.eth.getBalance(wallet_address)

print("get balance complete")

# convert to ether
balance_in_ether = web3.fromWei(balance, 'ether')

print("balance in eth complete")

print(f'The balance of {wallet_address} is {balance_in_ether} ether.')
print("final print complete")

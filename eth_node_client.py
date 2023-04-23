from web3 import Web3
from web3.contract import ConciseContract
import requests
import abi_util

# connect to the Ethereum client
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))


def get_puncher_info(token_id, name):
    # ABI of the ERC721 smart contract
    cockpunch_abi = abi_util.cockpunch_abi_str
    # address of the ERC721 token
    cockpunch_contract_address = '0xC178994cB9b66307Cd62dB8b411759Dd36D9C2EE'
    # create a contract instance
    cockpunch_token_contract = web3.eth.contract(address=cockpunch_contract_address, abi=cockpunch_abi)
    # create a concise contract instance for easier method calls
    cc = ConciseContract(cockpunch_token_contract)
    # Call the tokenURI() function of the contract to retrieve the metadata URI for the given token ID
    metadata_uri = cockpunch_token_contract.functions.tokenURI(token_id).call()

    # Use the metadata URI to retrieve the metadata JSON from the IPFS or HTTP endpoint
    metadata_json = requests.get(metadata_uri).json()

    # Extract the desired metadata fields from the metadata JSON
    attributes = metadata_json['attributes']

    clan = 'none'
    weapon = 'none'
    gauntlet = 'none'

    for attribute in attributes:
        if attribute['trait_type'] == 'Clan':
            clan = attribute['value']
        if attribute['trait_type'] == 'Weapon':
            weapon = attribute['value']
        if attribute['trait_type'] == 'Gauntlet':
            gauntlet = attribute['value']
    
    return f"{name} is a {clan}. He wields a {weapon} as a weapon and a {gauntlet} as a gauntlet"



def get_hv_mtl_info(token_id):
    # ABI of the ERC721 smart contract
    hv_mtl_abi = abi_util.hv_mtl_abi_str
    # address of the ERC721 token
    hv_mtl_contract_address = '0x4b15a9c28034dC83db40CD810001427d3BD7163D'
    # create a contract instance
    hv_mtl_token_contract = web3.eth.contract(address=hv_mtl_contract_address, abi=hv_mtl_abi)
    # Call the tokenURI() function of the contract to retrieve the metadata URI for the given token ID
    metadata_uri = hv_mtl_token_contract.functions.tokenURI(token_id).call()
    # Use the metadata URI to retrieve the metadata JSON from the IPFS or HTTP endpoint
    metadata_json = requests.get(metadata_uri).json()
    # Extract the desired metadata fields from the metadata JSON
    attributes = metadata_json['attributes']

    print("attributes:")
    print(attributes)

    return


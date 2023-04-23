from web3 import Web3
from web3.contract import ConciseContract
import json
import requests

print("imports complete")

# connect to the Ethereum client
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
print("connection complete")

# ABI of the ERC721 smart contract
abi = [{"inputs":[{"internalType":"address payable","name":"primaryReceiver_","type":"address"},{"internalType":"address payable","name":"royaltiesReceiver","type":"address"},{"internalType":"string","name":"baseTokenURI_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"BurnDisabled","type":"error"},{"inputs":[],"name":"CannotCommitAgain","type":"error"},{"inputs":[{"internalType":"enum Cockpunch.Stage","name":"got","type":"uint8"},{"internalType":"enum Cockpunch.Stage","name":"want","type":"uint8"}],"name":"DisallowedByCurrentStage","type":"error"},{"inputs":[],"name":"IllegalOperator","type":"error"},{"inputs":[{"internalType":"uint256","name":"got","type":"uint256"},{"internalType":"uint256","name":"want","type":"uint256"}],"name":"IncorrectPayment","type":"error"},{"inputs":[],"name":"InvalidAllowanceSignature","type":"error"},{"inputs":[],"name":"InvalidAmount","type":"error"},{"inputs":[],"name":"InvalidAmountZero","type":"error"},{"inputs":[],"name":"InvalidCommitment","type":"error"},{"inputs":[],"name":"InvalidPayment","type":"error"},{"inputs":[],"name":"InvalidValidatorAuthorizationSignature","type":"error"},{"inputs":[],"name":"ListHasEnded","type":"error"},{"inputs":[],"name":"ListNotStarted","type":"error"},{"inputs":[],"name":"MintERC2309QuantityExceedsLimit","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"NotAuthorized","type":"error"},{"inputs":[{"internalType":"address","name":"operator","type":"address"}],"name":"OperatorNotAllowed","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"OwnershipNotInitializedForExtraData","type":"error"},{"inputs":[],"name":"PleaseImplementMe","type":"error"},{"inputs":[],"name":"PremintMaxPerWalletReached","type":"error"},{"inputs":[],"name":"StageLocked","type":"error"},{"inputs":[],"name":"TooManyMintsRequested","type":"error"},{"inputs":[],"name":"TooManyRequested","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"WrongTarget","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"approved","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":False,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"fromTokenId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"toTokenId","type":"uint256"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"}],"name":"ConsecutiveTransfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"NUM_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OPERATOR_FILTER_REGISTRY","outputs":[{"internalType":"contract IOperatorFilterRegistry","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PREMINT_READY_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseTokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"burnEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"attributesURL","type":"string"},{"internalType":"bytes32","name":"saltHash","type":"bytes32"}],"name":"commit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"domainSeparator","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"entropy","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockStage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint16","name":"num","type":"uint16"}],"internalType":"struct Cockpunch.OwnerMintReceiver[]","name":"receivers","type":"tuple[]"}],"name":"ownerMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"ownerMintsRemaining","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"bytes32","name":"listId","type":"bytes32"},{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"startsAt","type":"uint256"},{"internalType":"uint256","name":"endsAt","type":"uint256"},{"internalType":"uint256","name":"unitPrice","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IPremintReady.AccountAllowance","name":"allowance","type":"tuple"},{"internalType":"bytes","name":"allowanceSignature","type":"bytes"},{"internalType":"address","name":"validator","type":"address"},{"internalType":"bytes","name":"validatorAuthorizationSignature","type":"bytes"}],"internalType":"struct IPremintReady.PremintConfig","name":"config","type":"tuple"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"premint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"premintAllowanceUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"premintMax","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"premintSigner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"premintWalletMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"primaryReceiver","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"amount","type":"uint16"}],"name":"reduceOwnerMintAllocation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"salt","type":"bytes32"}],"name":"revealEntropy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_baseTokenURI","type":"string"}],"name":"setBaseTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint96","name":"basisPoints","type":"uint96"}],"name":"setDefaultRoyalty","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"signer","type":"address"}],"name":"setPremintSigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"primaryReceiver_","type":"address"}],"name":"setPrimaryReciever","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"enum Cockpunch.Stage","name":"stage_","type":"uint8"}],"name":"setStage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stage","outputs":[{"internalType":"enum Cockpunch.Stage","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stageLocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"enabled","type":"bool"}],"name":"toggleBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}]

abi_str = json.dumps(abi)

print("abi set complete")
# address of the ERC721 token
contract_address = '0xC178994cB9b66307Cd62dB8b411759Dd36D9C2EE'

# create a contract instance
token_contract = web3.eth.contract(address=contract_address, abi=abi_str)
print("get eth contract complete")
# create a concise contract instance for easier method calls
cc = ConciseContract(token_contract)
print("convert to concise contract complete")
# get the name and symbol of the token
name = cc.name()
symbol = cc.symbol()
print("extract name and symbol complete")

print(f'The token at {contract_address} is {name} ({symbol}).')


def get_puncher_info(token_id):
    # Call the tokenURI() function of the contract to retrieve the metadata URI for the given token ID
    metadata_uri = token_contract.functions.tokenURI(token_id).call()

    print("get metadata uri complete")

    # Use the metadata URI to retrieve the metadata JSON from the IPFS or HTTP endpoint
    metadata_json = requests.get(metadata_uri).json()
    print("get metadata json complete")

    # Extract the desired metadata fields from the metadata JSON
    name = metadata_json['name']
    description = metadata_json['description']
    image_url = metadata_json['image']
    attributes = metadata_json['attributes']

    #print(f'name is {name} and description is {description} and image_url is {image_url}')


    print("attributes:")
    print(attributes)

    print(type(attributes))

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
    
    return f"{name} is a {clan}. He weilds a {weapon} as a weapon and a {gauntlet} as a gauntlet."

fighter_one_token_id = 4915
fighter_one_info = get_puncher_info(fighter_one_token_id)
print(fighter_one_info)

fighter_two_token_id = 3825
fighter_two_info = get_puncher_info(fighter_two_token_id)
print(fighter_two_info)

# TODO: connect this with opensea api to generate a fight based on two token ids.
# Other ideas: 
# Give users more freedom on which attributes are referenced. 
# Perhaps allow users to choose up to 4 attributes.
# Perhaps create a web page view where this all renders. Or somehow expose this,
# even if it's only available when I'm running it.
# Maybe there is something I can do with this related to mutant hounds or apecoin.

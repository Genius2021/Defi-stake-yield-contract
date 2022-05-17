from brownie import ElonToken, TokenFarm, config, network
from web3 import Web3

KEPT_BALANCE = Web3.toWei(100, "ether")

def deploy_token_farm_and_token():
    account = getAccount()
    elon_token = ElonToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(elon_token.address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify", False))
    tx = elon_token.transfer(token_farm.address, elon_token.totalSupply() - KEPT_BALANCE, {"from": account})
    tx.wait(1)

    #elon_token, weth_token, fau_token/dai
    weth_token = 
    add_allowed_tokens(token_farm)


def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):




def main():
    deploy_token_farm_and_token()
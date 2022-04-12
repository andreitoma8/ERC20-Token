from brownie import ERC20Token, accounts, config


def main():
    account = accounts.add(config["wallets"]["from_key"])
    my_token = ERC20Token.deploy(
        "Ethereum", "ETH", {"from": account}, publish_source=True
    )

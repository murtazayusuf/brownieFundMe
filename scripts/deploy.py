from brownie import accounts, network, config, FundMe, MockV3Aggregator
from web3 import Web3
from scripts.helper_scripts import get_account, get_price_feed


def deploy_fund_me():
    account = get_account()
    price_feed_address = get_price_feed()

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(fund_me.getPrice() / 10 ** 18)
    return fund_me


def main():
    deploy_fund_me()

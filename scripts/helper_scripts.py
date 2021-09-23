from brownie import accounts, network, config, MockV3Aggregator

FORKED_ENVIRONMENTS = ['mainnet-fork']
LOCAL_BLOCKCHAINS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAINS or network.show_active() in FORKED_ENVIRONMENTS:
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def get_price_feed():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"Active network is {network.show_active()}")
        print("Deploying Mocks...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(18, 3030 * 10 ** 8, {"from": account})
        mock_aggregator = MockV3Aggregator[-1]
        price_feed_address = mock_aggregator.address
        print("Mock Deployed!")
    return price_feed_address

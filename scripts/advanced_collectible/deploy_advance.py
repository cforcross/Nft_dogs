from brownie import accounts, network, AdvancedCollectible, config
from scripts.helpful_scripts import fund_advance_collectible


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    publish_source = False
    advance_collectible = AdvancedCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=publish_source,
    )
    fund_advance_collectible(advance_collectible)
    return advance_collectible

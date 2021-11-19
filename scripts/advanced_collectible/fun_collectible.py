from brownie import accounts, network, AdvancedCollectible, config
from scripts.helpful_scripts import fund_advance_collectible


def main():
    advance_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_advance_collectible(advance_collectible)

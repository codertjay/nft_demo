from scripts.helpful_scripts import (
    get_account, OPENSEA_URL, get_contract,
    fund_with_link)
from brownie import AdvancedCollectible, config, network

sample_token_uri = 'https://ipfs.io/ipfs/QmRDCFgA4ndTft2dE2UiwNxQVVXAPxJYnrtaNbhf6CGT5q?filename=texture.jpg'


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config['networks'][network.show_active()]['keyhash'],
        config['networks'][network.show_active()]['fee'],
        {'from': account}, publish_source=config['networks'][
            network.show_active()].get('verify', False))
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({'from': account})
    creating_tx.wait(1)
    print('New token was deployed!')

    print(
        f"Awesome, You can view your NFT at {OPENSEA_URL.format(advanced_collectible.address, advanced_collectible.tokenCounter() - 1)} ")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()

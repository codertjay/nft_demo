from scripts.helpful_scripts import get_account,OPENSEA_URL

from brownie import SimpleCollectible

sample_token_uri = 'https://ipfs.io/ipfs/QmRDCFgA4ndTft2dE2UiwNxQVVXAPxJYnrtaNbhf6CGT5q?filename=texture.jpg'


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({'from': account})
    tx = simple_collectible.createCollectible(
        sample_token_uri, {'from': account})
    tx.wait(1)
    print(
        f"Awesome, You can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)} ")
    return simple_collectible

def main():
    deploy_and_create()

from brownie import network

from scripts.advanced_collectible.deploy_and_create import (
    deploy_and_create, get_contract)
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
import pytest


def test_can_create_advanced_collectible():
    # deploy and create
    # create an NFT
    #  get a random breed
    #  Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, creating_transaction = deploy_and_create()
    requestId = creating_transaction.events['requestedCollectible']["requestId"]
    print('The requestId', requestId)
    random_number = 777
    get_contract(
        'vrf_coordinator').callBackWithRandomness(
        requestId, random_number,
        advanced_collectible.address,
        {'from': get_account()})
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3

import time

import pytest
from brownie import network

from scripts.advanced_collectible.deploy_and_create import (
    deploy_and_create)
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_advanced_collectible_integration():
    # deploy and create
    # create an NFT
    #  get a random breed
    #  Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, creating_transaction = deploy_and_create()
    time.sleep(60)
    assert advanced_collectible.tokenCounter() == 1

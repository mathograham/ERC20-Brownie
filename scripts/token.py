#!/usr/bin/python3

from brownie import Token, accounts, config


def main():
    account = accounts.add(config["wallets"]["from_key"])
    return Token.deploy("TestToken", "TST", 18, 1e21, {'from': account})

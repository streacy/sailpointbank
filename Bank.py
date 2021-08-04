from typing import Dict

import Account

"""
Bank keeps track of users by keeping a map of user name to Account instance.
Every time a new Account is created, it will add it to its map.

"""


class Bank:

    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def add_account(self, name, account):
        self.accounts[name] = account

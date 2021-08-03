from typing import Dict

import Account


class Bank:

    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def add_account(self, name, account):
        self.accounts[name] = account

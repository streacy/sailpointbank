import random
import unittest

from Account import Account
from Bank import Bank


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.name = random.sample
        self.pin = random.randint
        self.account = Account(self.name, self.pin)

    def test_add_account(self):
        self.bank.add_account(self.name, self.account)

        self.assertEqual(len(self.bank.accounts), 1)
        self.assertTrue(self.name in self.bank.accounts)

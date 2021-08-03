import random
import unittest

from Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.name = random.sample
        self.pin = random.randint
        self.account = Account(self.name, self.pin)

    def test_set_pin(self):
        self.assertEqual(self.pin, self.account.pin)

        new_pin = random.randint
        self.account.set_pin(new_pin)

        self.assertEqual(self.account.pin, new_pin)

    def test_get_pin(self):
        actual_pin = self.account.get_pin()

        self.assertEqual(actual_pin, self.pin)

    def test_withdraw(self):
        self.account.balance = 100
        self.account.withdraw(10)

        self.assertEqual(90, self.account.balance)

    def test_withdraw_over_limit(self):
        self.account.balance = 10
        self.account.withdraw(11)

        self.assertEqual(10, self.account.balance)

    def test_deposit(self):
        amount = 10
        self.account.deposit(amount)

        self.assertEqual(amount, self.account.balance)

    def test_get_balance(self):
        self.assertEqual(0, self.account.get_balance())
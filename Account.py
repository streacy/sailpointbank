class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin: int = pin
        self.balance: float = 0

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds, your current balance is ${}. You do not have enough to "
                  "withdraw ${}.".format(self.balance, amount))

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

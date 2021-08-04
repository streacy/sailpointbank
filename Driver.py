from Account import Account
from Bank import Bank


"""
Driver main method is running the program, and takes you through the process of logging in and performing 
bank transactions. There is a default account set up called admin. You can also create an account and log in
using the credentials you set. 

"""

def main():
    options = ["1", "2", "3", "4", "5"]
    bank = Bank()
    bank.add_account("admin", Account("admin", "0000"))
    while True:
        print("Welcome to SailPoint Bank")
        print("Please pick from the following options: ")
        # First main menu option
        option = input("1. Log in 2. Open Account 3.Exit: ")

        # If you choose to login
        if option == options[0]:
            user_name = input("Enter your name: ")
            pin = input("Enter your pin: ")

            # If you user name and password match the Bank records
            if user_name in bank.accounts and pin == bank.accounts[user_name].get_pin():
                while True:
                    print("Please pick from the following options: ")
                    option = input("1. View Balance 2. Deposit Money 3. Withdraw Money 4. Reset Pin 5.Exit: ")

                    if option == options[0]:
                        print("Your balance is ${}".format(bank.accounts[user_name].get_balance()))
                    elif option == options[1]:
                        deposit_amount = input("How much would you like to deposit: ")
                        bank.accounts[user_name].deposit(float(deposit_amount))
                        print("You have successfully deposited ${}".format(deposit_amount))
                    elif option == options[2]:
                        withdraw_amount = input("How much would you like to withdraw: ")
                        bank.accounts[user_name].withdraw(float(withdraw_amount))
                    elif option == options[3]:
                        reset_pin(bank, user_name)
                    elif option == options[4]:
                        break
                    else:
                        print("You have entered an invalid option, bringing you back to menu")

            # If you user name is in the bank records but your pin is incorrect
            elif user_name in bank.accounts and pin != bank.accounts[user_name].get_pin():
                print("Password is invalid, would you like to reset your password?")
                option = input("y/n: ")
                if option == "y" or option == "yes":
                    reset_pin(bank, user_name)
                elif option == "n" or option == "no":
                    pass
            # If neither your user name and pin is correct, you can open an account
            else:
                print("Account does not exist, would you like to open an Account?")
                option = input("y/n: ")
                if option == "y" or option == "yes":
                    open_account(bank, user_name)
                elif option == "n" or option == "no":
                    pass
        # Opening Account
        elif option == options[1]:
            user_name = input("Enter user name: ")
            open_account(bank, user_name)
        # Exit program
        elif option == options[2]:
            print("Thanks for stopping by!")
            break
        # All other cases for invalid options
        else:
            print("You have entered an invalid option, bringing you back to menu")
            pass

"""
This Method is used to create a new instance of Account and update the Bank map with it
"""
def open_account(bank, user_name):
    pin = input("Enter a pin number: ")
    account = Account(user_name, pin)
    bank.add_account(user_name, account)
    print("Congratulations {}, you have opened an account!".format(user_name))

"""
This method is used to reset the pin for a specific user 
which also in turn updated the Banks records.
"""
def reset_pin(bank, user_name):
    new_pin = input("Please enter your new pin: ")
    bank.accounts[user_name].set_pin(new_pin)


if __name__ == "__main__":
    main()
#Welcome to SailPoint Bank Interface

####Pre-requisite: Python version >= 3.0 

This python interface will allow you to do the following:
 1. Log into your account with a user name and pin
 2. Check balance
 3. Withdraw money
 4. Deposit money
 5. Open Account

####To run this in terminal, execute the following command:
```
python3 Driver.py
```
####To run this in an IDE:
Go to the Driver class Driver.py and run the main method.

Once the program has started, you will be brought to the main menu where it will ask you if you would like to
login or open an account.
By default, I have added a Customer with the following credentials:
    
    user name: admin
    pin: 0000
    
If you login with the default credentials, you will be able to view balance, deposit money, withdraw money
 or reset password.
 
You can also create an account by providing a user name and pin. If you try to login with a user name that
does not exist, it will ask if you would like to create an account. If you try to log in with an
incorrect pin, it will ask if you would like to reset the pin. 

Example Using program:


    > python3 Driver.py
    
    Welcome to SailPoint Bank
    Please pick from the following options: 
    1. Log in 2. Open Account 3.Exit:
    
    > 1
    
    Enter your name:
    
    > admin
    
    Enter your pin:
    
    > 0000
    
    Please pick from the following options: 
    1. View Balance 2. Deposit Money 3. Withdraw Money 4. Reset Pin 5.Exit:
    
    > 1
    
    Your balance is $0

    Please pick from the following options: 
    1. View Balance 2. Deposit Money 3. Withdraw Money 4. Reset Pin 5.Exit:
    
###Testing
To run the unit tests from the files TestAccount.py and TestBank.py you can run the following commands:

    python3 -m unittest TestAccount.py
    python3 -m unittest TestBank.py
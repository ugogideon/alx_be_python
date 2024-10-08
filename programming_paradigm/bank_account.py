# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
       """Initialize the account with an optional initial balance, default is zero."""
       self.__account_balance = initial_balance
    def deposit(self, amount):
        """Deposit a specific amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
                print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw a specific amount if sufficient balance is available."""
        if amount > self.__account_balance:
            return False    # Insufficient funds
        else:
            sself.__account_balance -= amount
            return True     # Successful withdrawal
    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
                                   
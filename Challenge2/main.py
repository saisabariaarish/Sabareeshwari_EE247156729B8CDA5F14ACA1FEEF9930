class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0) -> None:
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self) -> None:
        print(f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}")

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def account_holder_name(self) -> str:
        return self.__account_holder_name

    @property
    def account_balance(self) -> float:
        return self.__account_balance


# Create an instance of the BankAccount class
bank_account = BankAccount(account_number="1234567890", account_holder_name="John Doe")

# Test the deposit and withdrawal functionality
bank_account.deposit(1000)
bank_account.withdraw(500)
bank_account.display_balance()



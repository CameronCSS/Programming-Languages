class BankAccount:
    def __init__(self, name, initial_balance = 0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if (amount >= 0):
            self.balance += amount
            print("\n -----------SUCCESS-----------")
            print(f"\nSuccesfully deposited ${amount:.2f}")
            print(f"Balance: ${self.balance:.2f}")
        else:
            print("\n -----------ERROR-----------")
            print("\nInvalid Deposit!")

    def withdraw(self, amount):
        if(amount > self.balance):
            print("\n -----------ERROR-----------")
            print("\nInsufficient Funds!")
            print(f"Current Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print("\n -----------SUCCESS-----------")
            print(f"\nSuccesfully Withdrew ${amount:.2f}")
            print(f"Balance: ${self.balance:.2f}")
        
    def show_balance(self):
        print("\n -----------BALANCE-----------")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")
import BankAccount

def main():
    print("Welcome!!")
    print("----BANK ACCOUNT SYSTEM----")
    print("---------------------------")

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Please enter a name")
            continue

        try:
            deposit = float(input("Enter initial deposit amount: "))
            if deposit <= 0:
                print("Deposit must be greater than 0")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        break

    account = BankAccount.BankAccount(name, deposit)

    while True:
        print("\nOptions:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Balance")
        print("4: Exit")

        choice = input("Enter your choice: ")

        match (choice):
            case "1":
                deposit = float(input("Enter amount to Deposit: "))
                if(deposit <=0):
                    print("\n----------------")
                    print("\nInvalid amount!")
                    break
                account.deposit(deposit)
            case "2":
                withdraw = float(input("Enter amount to Withdraw: "))
                if(withdraw <=0):
                    print("\n----------------")
                    print("\nInvalid amount!")
                    break
                account.withdraw(withdraw)
            case "3":
                account.show_balance()
            case "4":
                print("\nThanks for using our System!!")
                print("----Goodebye!!----")
                print()
                break
            case _:
                print("\n----------------")
                print("Invalid Choice!!")

        
main()

    
    
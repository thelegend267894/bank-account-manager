# ---BANK ACCOUNT MANAGER---

# MAIN STORAGE DICTIONARY
Accounts = {}

# --- FUNCTIONS --- #

# Verify account existence
def verify(account: str):
    return account in Accounts

# Create an account
def create(name: str):
    if verify(name):
        print("⚠️ Account already exists.")
        return
    Accounts[name] = {"Balance": 0, "Transactions": []}
    print(f'✅ Created account named "{name}"')

# Deposit money
def deposit(name: str, amount: float):
    if not verify(name):
        print("❌ Account does not exist")
        return
    amount = round(amount, 2)
    if amount > 0:
        Accounts[name]["Balance"] += amount
        Accounts[name]["Transactions"].append(f"Deposited ${amount:.2f}")
        print(f'💰 Deposited ${amount:.2f} to {name}')
    else:
        print("❌ Invalid deposit amount.")

# Withdraw money
def withdraw(name: str, amount: float):
    if not verify(name):
        print("❌ Account does not exist")
        return
    amount = round(amount, 2)
    if amount > 0 and Accounts[name]["Balance"] >= amount:
        Accounts[name]["Balance"] -= amount
        Accounts[name]["Transactions"].append(f"Withdrew ${amount:.2f}")
        print(f'💸 Withdrew ${amount:.2f} from {name}')
    else:
        print("❌ Withdrawal failed (invalid amount or insufficient funds).")

# Transfer money
def transfer(sender: str, receiver: str, amount: float):
    if not verify(sender) or not verify(receiver):
        print("❌ One or both accounts do not exist")
        return
    amount = round(amount, 2)
    if amount > 0 and Accounts[sender]["Balance"] >= amount:
        Accounts[sender]["Balance"] -= amount
        Accounts[sender]["Transactions"].append(f'${amount:.2f} was sent to {receiver}')
        Accounts[receiver]["Balance"] += amount
        Accounts[receiver]["Transactions"].append(f'Received ${amount:.2f} from {sender}')
        print(f'💱 Transferred ${amount:.2f} from {sender} to {receiver}')
    else:
        print("❌ Transfer failed (invalid amount or insufficient funds).")

# View account details
def view(name: str):
    if not verify(name):
        print("❌ Account does not exist")
        return
    print("\n--- ACCOUNT DETAILS ---\n")
    print(f'Account: {name}')
    print(f'Balance: ${round(Accounts[name]["Balance"], 2)}')
    print("Transactions:")
    for element in Accounts[name]["Transactions"]:
        print("--> ", element)
    print("------------------------\n")

# Apply interest
def apply_interest(name: str):
    global interest, interest_val
    if not verify(name):
        print("❌ Account does not exist")
        return
    if interest:
        bonus = Accounts[name]["Balance"] * (interest_val / 100)
        Accounts[name]["Balance"] += bonus
        Accounts[name]["Transactions"].append(f"Interest applied: ${bonus:.2f}")
        print(f"💹 Interest applied to {name}: ${bonus:.2f}")
    else:
        print("❌ Interest is turned OFF.")

# Delete account
def delete(name: str):
    if not verify(name):
        print("❌ Account does not exist")
        return
    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
    if confirm == "y":
        del Accounts[name]
        print(f"🗑️ Account '{name}' has been deleted.")
    else:
        print("❎ Deletion canceled.")

# View all accounts sorted
def view_all_sorted():
    if not Accounts:
        print("⚠️ No accounts to display.")
        return
    print("\n--- ALL ACCOUNTS ---\n")
    for name in sorted(Accounts):
        balance = Accounts[name]["Balance"]
        print(f"Account: {name} | Balance: ${balance:.2f}")
    print("------------------------------------------\n")

# --- MENU LOOP --- #
interest = False
interest_val = 0

while True:
    print("\n========== BANK ACCOUNT MANAGER ==========\n")
    print("1) Create an Account")
    print("2) Deposit Amount")
    print("3) Withdraw Amount")
    print("4) Transfer Amount")
    print("5) View Account")
    print(f"6) Toggle Interest: {'ON' if interest else 'OFF'}")
    print(f"7) Interest Value: {interest_val}%")
    print("8) Apply interest to an account")
    print("9) Delete Account")
    print("10) View all accounts")
    print("11) Exit")
    print("\n==========================================")

    user_choice = input("Enter the choice number: ")

    if user_choice == "1":
        create(input("Enter the account name: "))

    elif user_choice == "2":
        account_name = input("Enter the account to deposit to: ")
        try:
            amount = float(input("Enter the amount to deposit: "))
        except ValueError:
            print("❌ Invalid amount entered.")
        else:
            deposit(account_name, amount)

    elif user_choice == "3":
        account_name = input("Enter the account to withdraw from: ")
        try:
            amount = float(input("Enter the amount to withdraw: "))
        except ValueError:
            print("❌ Invalid amount entered.")
        else:
            withdraw(account_name, amount)

    elif user_choice == "4":
        sender = input("Enter the account you want to transfer from: ")
        receiver = input("Enter the account you want to transfer to: ")
        try:
            amount = float(input("Enter the amount of money needed transfer: "))
        except ValueError:
            print("❌ Invalid amount entered.")
        else:
            transfer(sender, receiver, amount)

    elif user_choice == "5":
        view(input("Enter the name of the account: "))

    elif user_choice == "6":
        interest = not interest
        print(f"✅ Interest is now {'ON' if interest else 'OFF'}")

    elif user_choice == "7":
        try:
            interest_val = float(input("Enter the amount of interest (in percentage): "))
        except ValueError:
            print("❌ Invalid interest value entered.")
        else:
            print(f"✅ Interest value set to {interest_val}%")

    elif user_choice == "8":
        apply_interest(input("Enter account name: "))

    elif user_choice == "9":
        delete(input("Enter the account you want to delete: "))

    elif user_choice == "10":
        view_all_sorted()

    elif user_choice == "11":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 11.")

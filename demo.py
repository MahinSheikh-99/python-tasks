class BankAccount:
    def __init__(self):
        self.balance = 0

    def create_account(self):
        print("Account created successfully!")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"Amount {amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.balance}")

    def account_detail(self):
        print(f"Account balance: {self.balance}")


print("Hello! Welcome to XYZ Bank")
print("Please select an option")
print("1 = Create Your Account\n2 = Deposit Amount\n3 = Withdraw Amount\n4 = Account Detail\n0 = Exit")

account = None

while True:
    key = int(input("Enter Your Value = "))
    if key == 0:
        print("Exiting...")
        break
    elif key == 1:
        if account is None:
            account = BankAccount()
            account.create_account()
        else:
            print("Account already exists!")
    elif key == 2:
        if account is not None:
            account.deposit()
        else:
            print("You need to create an account first.")
    elif key == 3:
        if account is not None:
            account.withdraw()
        else:
            print("You need to create an account first.")
    elif key == 4:
        if account is not None:
            account.account_detail()
        else:
            print("You need to create an account first.")
    else:
        print("Invalid Option")
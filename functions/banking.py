class BankAccount:
    def __init__(self):
        self.balance = 0

    def create_account(self):
        print("Hello! Welcome to XYZ Bank")
        self.name = input("Enter name = ")
        self.account_no = int(input("Enter Account no = "))
        print("Account created successfully!")

    def account_detail(self):
        print("Hello! Welcome to XYZ Bank \nyour account Details is here")
        print("User Name = ", self.name, "\nAccount No = ", self.account_no, "\nBalance = ", self.balance)

    def deposit(self):
        print("****** Deposite Amount ******")
        amount = float(input("Enter Deposite Amount = "))
        self.balance += amount
        print("Amount Deposited = ", amount)
        print("Total Amount After Deposited = ", self.balance)

    def Withdrew(self):
        print("****** Withdraw Amount ******")
        withdrew_amount = float(input("Enter Withdraw Amount = "))
        if(self.balance >= withdrew_amount):
            self.balance -= withdrew_amount
            print("Amount Withdrew = ",  withdrew_amount)
            print("Remain Amount After Withdraw = ", self.balance)

        else:
            print("insufficient Balance")

print("Hello! Welcome to XYZ Bank \nplease select option")
print("1 = Create Your Account \n2 = Deposite Amount \n3 = Withdraw Amount \n4 = account_detail \n0 = exit")

account = None

while True:
    key = int(input("Enter Your Value = "))
    if key == 0:
        print("Exiting...")
        break
    elif (key == 1):
        if (account == None):
            account = BankAccount()
            account.create_account()
        else:
            print("Account already exists!")
    elif(key == 2):
        if (account != None):
            account.deposit()  # here call function through object of BankAccount Class
        else:
            print("You need to create an account first.")
    elif(key == 3):
        if (account != None):
            account.Withdrew()  # here call function through object of BankAccount Class
        else:
            print("You need to create an account first.")
    elif(key == 4):
        if (account != None):
            account.account_detail()  # here call function through object of BankAccount Class
        else:
            print("You need to create an account first.")
    else:
        print("Invalid Option")
bankName = (str(input("Enter your bank name :")))
name = (str(input("Enter your name :")))
branch = (str(input("Enter your branch address :")))
ac = (int(input("Enter your account number :")))
balance = (int(input("Enter your current balance :")))
def deposit(amount,balance):
    if 0>amount:
            print("Invalid amount")
            exit(0)
    balance = int(balance) + amount
    print("New Balance : ",balance)
    return balance
def withdraw(amount,balance):
        balance = int(balance) - amount
        print("New Balance : ",balance)
        return balance
def display():
     print("Bank Name : ",bankName)
     print("Name : ",name)
     print("Branch : ",branch)
     print("Account Number : ",ac)
     print("Balance : ",balance)

if 0>balance:
    print("Invalid balance")
    exit(0)
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        amount = int(input("Enter the amount to be deposited : "))
        balance = deposit(amount,balance)
    elif choice == 2:
        amount = int(input("Enter the amount to be withdrawn : "))
        balance = withdraw(amount,balance)
    elif choice == 3:
        display()
    elif choice == 4:
        break

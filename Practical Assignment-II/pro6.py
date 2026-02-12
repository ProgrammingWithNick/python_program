# 6. Banking System Using Functions

balance = 1000.0

def deposit(balance, amount):
    balance = balance + amount
    print("Amount Deposited:", amount)
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Amount Withdrawn:", amount)
    return balance

def check_balance(balance):
    print("Current Balance:", balance)

while True:
    print("\nBanking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        balance = deposit(balance, amt)
        
    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        balance = withdraw(balance, amt)
        
    elif choice == 3:
        check_balance(balance)
        
    elif choice == 4:
        print("Thank you for using Banking System")
        break
        
    else:
        print("Invalid Choice")

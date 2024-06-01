class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount >= 500:
            self.balance -= withdraw_amount
            print("Amount successfully withdrawn")
        else:
            print("Insufficient balance.\nYou have to keep at least Rs. 500 in your account")

    def display(self):
        print("Your bank balance is:", self.balance)

account = BankAccount()
for _ in range(50):
    print("1. Deposit 2. Withdraw 3. Display 4. Exit")
    choice = int(input("Enter your choice: "))  # Use 'choice' instead of 'p' for clarity

    if choice == 1:
        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)
    elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)
    elif choice == 3:
        account.display()
    elif choice == 4:
        break
    else:
        print("You have entered a wrong value")

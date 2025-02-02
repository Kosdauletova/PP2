class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Replenishment for {amount}. New balance is {self.balance}")
        else:
            print("The deposit amount must be more than 0.")


    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -=amount
                print(f"Withdrawn {amount}. New balance is {self.balance}")
            else:
                print("Insufficient funds in the withdrawal account")
        else:
            print("The withdrawal amount must be grfeater than 0.")

    def get_balance(self):
        return self.balance
    

owner = input()
initial_balance = float(input())

#объект счета
account = Account(owner, initial_balance)

#что бы отображать текущий баланс
print(f" {owner} 's balance is: {account.get_balance()}")

#пополняем счет
deposit_amount = float(input())
account.deposit(deposit_amount) 

#снятие средств
withdraw_amount = float(input())
account.withdraw(withdraw_amount)

#проверяем текущий баланс
print(f"{owner} 's current balance is {account.get_balance()}")

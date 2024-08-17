from os import system
class CreditCard:
    def __init__(self, customer, bank, account, maxLimit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.maxLimit = maxLimit
        self.balance = 0
    
    def get_balance(self):
        return self.balance
    
    def charge(self, price):
        if price - self.balance > self.maxLimit:
            return False
        else:
            self.balance -= price
            return True
    
    def make_payment(self, amount):
        self.balance += amount
        return

    def __str__(self):
        return f'Customer: {self.customer}\nBank: {self.bank}\nAccount: {self.account}\nLimit: {self.maxLimit}\nBalance: {self.balance}'


cc = CreditCard('Lannister', 'Iron Bank', '5256321092573187', 1000)
print(cc)
choice = int(input("====Enter 1 to charge, 2 to make payment, 3 to exit\n"))
while choice != 3:
    system('cls')
    if choice == 1:
        print("====Enter amount to charge")
        amount = int(input())
        if cc.charge(amount):
            print("====Charge successful")
        else:
            print("====Charge failed")
    elif choice == 2:
        print("====Enter amount to make payment")
        amount = int(input())
        cc.make_payment(amount)
        print("====Payment successful")
    print(cc)
    print("====Enter 1 to charge, 2 to make payment, 3 to exit\n")
    choice = int(input())
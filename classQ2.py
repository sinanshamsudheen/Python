class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("total balance is: ",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was Credited.")
        print("total balance is: ",self.get_balance())

    
    def get_balance(self):
        return self.balance

acc1 = Account(5000,41303826518)
print(acc1.balance)
acc1.debit(2000)
acc1.credit(9000)

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}  \nAccount balance: ${self.balance}'

    def deposit(self, money):
        self.balance = self.balance + money
        return 'Deposit Accepted'

    def withdraw(self, money):
        if money > self.balance:
            return 'Funds Unavailable!'
        else:
            self.balance = self.balance - money
            return 'Withdrawal complete!'

if __name__ == '__main__':
    acc1 = Account('Jose', 100)
    print(acc1)
    print(acc1.owner)
    print(acc1.balance)
    print(acc1.deposit(100))
    print(acc1.withdraw(2))

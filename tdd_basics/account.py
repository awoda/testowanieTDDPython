class Account(object):

    def __init__(self, account_number, name, surname, account_balance):
        self.accountNumber = account_number
        self.name = name
        self.surname = surname
        self.accountBalance = account_balance

    def __call__(self, *args, **kwargs):
        return self.accountNumber

    def __str__(self):
        return self.accountNumber

    def owner(self):
        return self.name + " " + self.surname

    def balance(self):
        return self.accountBalance

    def number(self):
        return self.accountNumber

    def transfer(self, transfer_amount):
        self.accountBalance += transfer_amount

    def withdraw(self, moneyAmount):
        if (self.accountBalance >= moneyAmount):
            self.accountBalance -= moneyAmount

    def sendMoney(self, account, moneyAmount):
        if moneyAmount<0:
            return
        if (self.accountBalance >= moneyAmount):
            self.accountBalance -= moneyAmount
            account.accountBalance += moneyAmount

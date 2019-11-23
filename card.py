class Card(object):

    def __init__(self, account, pin):
        self.account = account
        self.pin = pin

    def __call__(self, *args, **kwargs):
        return self.account.owner()

    def check_pin(self, pin):
        if self.pin == pin:
            return True
        return False

    def get_account(self):
        return self.account

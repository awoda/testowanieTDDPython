class CardLockedException(BaseException):
    pass


class AnotherException(BaseException):
    pass


class Card(object):
    def __init__(self, account, pin):
        self.is_locked = False
        self.incorrect_pin_counter = 0
        self.account = account
        self.pin = pin

    def __call__(self, *args, **kwargs):
        return self.account.owner()

    def check_pin(self, pin):
        if self.incorrect_pin_counter >= 3:
            raise CardLockedException()
        if self.pin == pin:
            self.incorrect_pin_counter = 0
            return True
        self.incorrect_pin_counter += 1
        return False

    def get_account(self):
        return self.account

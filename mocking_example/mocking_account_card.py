from unittest.mock import patch

from tdd_basics.account import *
from tdd_basics.card import *


if __name__ == "__main__":
    with patch.object(Account, "owner", return_value="Bronislaw Mockowy", autospec=True):
        account = Account(name="Adrian", account_number="1234567890", surname="Woda", account_balance=20000.00)
        card = Card(account, "1234")
        print (card())




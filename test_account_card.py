import unittest
import os

from account import Account
from card import Card


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("1234567890", "Adrian", "Woda", 15000 * 1.23)
        self.card = Card(self.account, 0000)

    def test_account_should_return_account_number(self):
        self.assertEqual(self.account(), "1234567890", "Account number not match")


    def test_owner_should_return_name_and_surname(self):
        self.assertEqual(self.account.owner(), "Adrian Woda", "Owner name not match")

    def test_balance_should_return_current_account_balance(self):
        self.assertEqual(self.account.balance(), 18450)

    def test_number_should_return_proper_acc_num(self):
        self.assertEqual(self.account.number(), "1234567890", "Account number not match")

    def test_transfer_should_properly_add_money(self):
        self.account.transfer(1550)
        self.assertEqual(self.account.balance(), 20000)

    def test_transfer_should_properly_substract_money(self):
        self.account.transfer(-3450)
        self.assertEqual(self.account.balance(), 15000)

    def test_card_should_return_owner_name(self):
        self.assertEqual(self.card(), "Adrian Woda")

    def test_check_pin_should_work_properly(self):
        self.assertFalse(self.card.check_pin(1234))
        self.assertTrue(self.card.check_pin(0000))

    def test_card_should_return_proper_account(self):
        self.assertIs(self.card.get_account(), self.account)

if __name__ == '__main__':
    unittest.main()

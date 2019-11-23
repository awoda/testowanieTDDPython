import unittest
import os
from account import Account
from card import Card, CardLockedException, AnotherException


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.account = Account(name="Adrian", account_number="1234567890", surname="Woda", account_balance=20000.00)

    def test_env_variable(self):
        self.assertEqual(os.environ['zmienna'], "123")

    def test_something(self):
        self.assertEqual(self.account(), "1234567890")

    def test_should_return_proper_owner_name(self):
        self.assertEqual(self.account.owner(), "Adrian Woda")

    def test_should_return_account_balance(self):
        self.assertEqual(self.account.balance(), 20000.00)

    def test_should_return_account_number(self):
        self.assertEqual(self.account.number(), "1234567890")

    def test_should_properly_transfer_money(self):
        self.account.transfer(-150)
        self.assertEqual(self.account.balance(), 19850)

    def test_should_properly_transfer_money2(self):
        self.account.transfer(1000)
        self.assertEqual(self.account.balance(), 21000)

    def test_should_card_return_owner_name(self):
        card = Card(self.account, "0000")

        self.assertEqual(card(), "Adrian Woda")

    def test_should_check_pin(self):
        card = Card(self.account, "0000")

        self.assertTrue(card.check_pin("0000"))
        self.assertFalse(card.check_pin("2345"))

    def test_should_card_return_proper_account(self):
        card = Card(self.account, "0000")

        self.assertEqual(card.get_account(), self.account)

    def test_should_withdraw_money_from_account(self):
# 2.        chce sprawdzic, czy po wyplacie, moj balance zmniejszyl się
        self.account.withdraw(500)
        self.assertEqual(self.account.balance(), 19500)

    def test_should_withdraw_money_from_account2(self):
# 1.        chce sprawdzic, czy moge wyciagnac wiecej niz mam
        self.account.withdraw(25000)
        self.assertEqual(self.account.balance(), 20000)

    def test_should_withdraw_money_from_account3(self):
# 1.        chce sprawdzic, czy moge wyciagnac wszystko
        self.account.withdraw(20000)
        self.assertEqual(self.account.balance(), 0)


    def test_should_send_money_to_another_account(self):
        account2 = Account(name="John", surname="Doe", account_number="0987654321", account_balance=20000.00)
        self.account.sendMoney(account2, 10)
        self.assertEqual(self.account.balance(), 20000-10)
        self.assertEqual(account2.balance(), 20000+10)

    def test_should_send_money_to_another_account2(self):
        account2 = Account(name="John", surname="Doe", account_number="0987654321", account_balance=20000.00)
        self.account.sendMoney(account2, 21000)
        self.assertEqual(self.account.balance(), 20000)
        self.assertEqual(account2.balance(), 20000)

    def test_should_not_be_able_to_send_negative_amount_of_money(self):
        account2 = Account(name="John", surname="Doe", account_number="0987654321", account_balance=20000.00)
        self.account.sendMoney(account2, -1000)
        self.assertEqual(self.account.balance(), 20000, "account1 balance mismatch")
        self.assertEqual(account2.balance(), 20000, "account2 balance mismatch")

    def test_should_cart_be_blocked_after_3_incorret_attempts(self):
        cart = Card(account=self.account, pin="1234")
        cart.check_pin("0000")
        cart.check_pin("0000")
        cart.check_pin("0000")

        with self.assertRaises(CardLockedException):
            cart.check_pin("1234")

    def test_should_cart_not_be_blocked_after_2_incorrect_attempts(self):
        cart = Card(account=self.account, pin="1234")
        cart.check_pin("0000")
        cart.check_pin("0000")

        self.assertTrue(cart.check_pin("1234"))

    def test_x(self):
        cart = Card(account=self.account, pin="1234")
        cart.check_pin("0000")
        cart.check_pin("0000")
        cart.check_pin("1234")
        cart.check_pin("0000")

        self.assertTrue(cart.check_pin("1234"))



if __name__ == '__main__':
    unittest.main()

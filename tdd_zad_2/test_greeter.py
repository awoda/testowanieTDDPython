import unittest
from greeter import greet


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(greet("Adrian"), "Hello Adrian.")

    def test_2(self):
        self.assertEqual(greet(), "Hello my friend.")

    def test_3(self):
        self.assertEqual(greet("ADAM"), "HELLO ADAM!")

    def test_4(self):
        self.assertEqual(greet("Magda", "John"), "Hello Magda, and John.")

    def test_5(self):
        self.assertEqual((greet("Magda", "John", "Peter")), "Hello Magda, John, and Peter.")

    def test_6(self):
        self.assertEqual(greet("Magda", "JOHN", "Peter"), "Hello Magda, and Peter. AND HELLO JOHN!")
        self.assertEqual(greet("Magda", "JOHN", "Peter", "GUSTAW"),
                         "Hello Magda, and Peter. AND HELLO JOHN, AND GUSTAW!")

    def test_7(self):
        self.assertEqual(greet("Magda", "JOHN, Peter"), "Hello Magda, and Peter. AND HELLO JOHN!")
        self.assertEqual(greet("Magda, JOHN, Peter, GUSTAW"), "Hello Magda, and Peter. AND HELLO JOHN, AND GUSTAW!")
        self.assertEqual(greet("Magda,JOHN,Peter,GUSTAW"), "Hello Magda, and Peter. AND HELLO JOHN, AND GUSTAW!")


if __name__ == '__main__':
    unittest.main()

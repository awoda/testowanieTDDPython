import unittest
from test_basics import MyFirstTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyFirstTest("test_1"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

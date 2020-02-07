import unittest


def setUpModule():
    print("module setup")

def tearDownModule():
    print ("module teardown")


class MyFirstTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Class set up")

    @classmethod
    def tearDownClass(cls):
        print("Class teardown")

    def setUp(self):
        print("Set Up for test")

    def tearDown(self):
        print("TearDown for test")

    @unittest.expectedFailure
    def test_1(self):
        print("prownuje 2 i 3")
        self.assertEqual(2, 3)

    def test_2(self):
        print("porownuje 2 i 2")
        self.assertEqual(2, 2)

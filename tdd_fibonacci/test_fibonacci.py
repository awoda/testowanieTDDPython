import unittest
from parameterized import parameterized, parameterized_class
from fibonacci import fibonacci, fibonacci_loop


@parameterized_class(('n', 'value'), [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (19, 4181)
])
class MyTestCase(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(self.n), self.value)

    def test_fibonacci_loop(self):
        self.assertEqual(fibonacci_loop(self.n), self.value)


if __name__ == '__main__':
    unittest.main()

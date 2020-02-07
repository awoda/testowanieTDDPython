import unittest
from unittest.mock import Mock
from parameterized import parameterized, parameterized_class

from module1 import attack_damage
from unittest import mock


class TestCase(unittest.TestCase):

    @parameterized.expand(["foo", "bar"])
    def test_sequence(self, name):
        print(name)


@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
   (1, 2, 3, 2),
   (5, 5, 10, 25),
])
class ParameterizedTestCase(unittest.TestCase):
   def test_add(self):
      self.assertEqual(self.a + self.b, self.expected_sum)

   def test_multiply(self):
      self.assertEqual(self.a * self.b, self.expected_product)



if __name__ == '__main__':
    unittest.main()

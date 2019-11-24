import unittest
from unittest.mock import Mock
from parameterized import parameterized, parameterized_class

from module1 import attack_damage
from unittest import mock


class Module1Tests(unittest.TestCase):

    @mock.patch("module1.randint", return_value=1, autospec=True)
    def test(self, mocked_randint):
        self.assertEqual(attack_damage(500), 500)

    def test_patch_with_context_manager(self):
        with mock.patch("module1.randint", return_value = 1, autospec=True):
            self.assertEqual(attack_damage(500), 500)

    def test2(self):
        mock = Mock()
        mock.x = "zmienna x"
        mock.funkcja_x = Mock(return_value="wartosc zwrocona przez funkcje")
        mock.funckja_rzucajaca_wyjatek = Mock(side_effect = BaseException("Rzucilem wyjatkiem"))
        print(mock.x)
        print(mock.funkcja_x())
        with self.assertRaises(BaseException):
            mock.funckja_rzucajaca_wyjatek()

    @parameterized.expand(["foo", "bar"])
    def test_sequence(self, name):
        print(name)


@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
   (1, 2, 3, 2),
   (5, 5, 10, 25),
])
class TestMathClass(unittest.TestCase):
   def test_add(self):
      self.assertEqual(self.a + self.b, self.expected_sum)

   def test_multiply(self):
      self.assertEqual(self.a * self.b, self.expected_product)



if __name__ == '__main__':
    unittest.main()

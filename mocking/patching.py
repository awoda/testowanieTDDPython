from unittest.mock import patch, create_autospec
from module1 import ClassToBePatched


class SomeClass():

    def something(self, arg1):
        return "something"


if __name__ == "__main__":
    with patch.object(SomeClass, "something", return_value="patched", autospec=True):
        some_class = SomeClass()
        print(some_class.something("asd"))
        print(some_class.something())

    with patch.object(ClassToBePatched, "function", return_value="patched again", autospec=True):
        patchedClass = ClassToBePatched()
        print(patchedClass.function())

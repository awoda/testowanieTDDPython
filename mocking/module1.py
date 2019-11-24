from random import randint


class ClassToBePatched():
    def function(self):
        return "something"


def attack_damage(modifier):
    roll = randint(1, 6)
    return roll * modifier

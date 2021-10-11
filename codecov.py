
from random import randint
import unittest


class RollableDie:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

class DiceBag:
    def __init__(self, dice_sides=[]):
        self.dice = self.create_dice_from_sides(dice_sides)

    def create_dice_from_sides(self, sides):
        return list(map(lambda side: RollableDie(side), sides))

    def roll_bag(self):
        return list(map(lambda dice: dice.roll(), self.dice))

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = RollableDie()

    def test_upper(self):
        self.assertEqual(self.die.sides, 6)
import unittest
from nhcalc import wishparser


class TestWishParser(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(wishparser.parsewish('nothing'), None)

    def test_buc(self):
        cases = (
            ('holy potion', 'blessed'),
            ('uncursed potion', 'uncursed'),
            ('unholy potion', 'cursed'),
            ('blessed uncursed cursed potion', 'cursed'),
            ('holy uncursed potion', 'uncursed')
            )
        for case in cases:
            item = wishparser.parsewish(case[0])
            self.assertEqual(item.buc, case[1])

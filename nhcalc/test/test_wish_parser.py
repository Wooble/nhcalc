import unittest
from nhcalc import wishparser

class TestWishParser(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(wishparser.parsewish('nothing'), None)


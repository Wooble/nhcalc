import unittest
from nhcalc import wishparser

class TestWishParser(unittest.TestCase):
    def test_nothing(self):
        self.AssertEqual(wishparser.parsewish('nothing'), None)


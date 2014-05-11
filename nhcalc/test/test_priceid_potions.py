import unittest
import nhcalc

class TestBuyPotions(unittest.TestCase):
    def test_healing(self):
        possibles = nhcalc.priceid.buy(price=100, description='fizzy potion')
        self.assertIn('potion of healing', possibles)

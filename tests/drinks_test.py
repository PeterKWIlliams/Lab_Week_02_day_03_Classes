import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):


    def setUp(self):
        
      self.drinks = Drink("Guiness",  5.00, True)

    def test_drink_has_name(self):
      
      self.assertEqual("Guiness",self.drinks.name) 

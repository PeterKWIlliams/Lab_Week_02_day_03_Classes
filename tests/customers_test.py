import unittest

from src.customers import Customers

class TestCustomers(unittest.TestCase):

    def setUp(self):
      
      self.customers = Customers("John", 50)

    def test_customers_has_name(self):

      self.assertEqual("John", self.customers.name)
    

    
    

    
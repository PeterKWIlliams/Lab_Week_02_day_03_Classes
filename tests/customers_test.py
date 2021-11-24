import unittest

from src.customers import Customers

class TestCustomers(unittest.TestCase):

    def setUp(self):
      
      self.customers = Customers("John",50,18)

    def test_customers_has_name(self):

      self.assertEqual("John", self.customers.name)
    
    def test_customer_has_paid(self):
        
        self.customers.pay_for_drink(5)
        
        self.assertEqual(45,self.customers.wallet)

    def test_customer_received_drink(self):
        
        self.customers.give_drink("guiness")
        
        self.assertEqual(self.customers.stomach[0],"guiness")
    
    

    
    

    
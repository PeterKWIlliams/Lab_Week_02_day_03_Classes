import unittest 
from src.pub import Pub
from src.customers import Customers

class TestPub(unittest.TestCase):

    def setUp(self):
      self.customer_1 = Customers("John",50,18)
      self.customer_2= Customers("jill", 70,16)
      self.pub = Pub("The Prancing Pony",100.00)
      
    def test_pub_has_name(self):
      
      self.assertEqual("The Prancing Pony",self.pub.name)

    def test_pub_has_been_paid(self):
      
       self.pub.receive_payment(5)
      
       self.assertEqual(105.00,self.pub.cash)
    
    def test_customer_of_age(self):
      
      self.assertEqual(True, self.pub.check_age(self.customer_1))
    
    
 
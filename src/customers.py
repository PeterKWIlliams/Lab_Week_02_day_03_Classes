
class Customers:
    def __init__ (self, name, wallet):
      
        self.name = name 
        self.stomach = []
        self.wallet = wallet      

    def pay_for_drink(self,amount):

        self.wallet -= amount 
        
        

    
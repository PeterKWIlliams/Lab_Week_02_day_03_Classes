
class Customers:
    def __init__ (self, name, wallet, age):
        
        self.drunkness = 0
        self.name = name 
        self.stomach = []
        self.wallet = wallet      
        self.age = age
    
    def pay_for_drink(self,amount):

        self.wallet -= amount 

    def give_drink(self,drink):
        
        self.stomach.append(drink)
    
    def get_turnt(self):
         
        self.drunkness += 

    
   
    
            


        
        

    
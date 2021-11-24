class Pub:
    def __init__(self,name,cash):
        
        self.name = name
        self.cash = cash 
        self.drnks= []
    def receive_payment(self,amount):
        
        self.cash += amount 
    
    # def sell_drinks_to_customers(self,customers):

    def check_age(self,customer):
        
        if customer.age >= 18:
           return True
        else:
            return False
            
        
        
        
        
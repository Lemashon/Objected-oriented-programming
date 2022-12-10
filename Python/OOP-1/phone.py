
from item import Item

class Phone(Item):
    #Child class     
    def __init__(self, name: str, price: float, quantity = 0, broken_phones=0):
        
        #Call to su[er function to have access to all attributes/methods
        #run validations to received arguments
        
        
        super().__init__(
            name,price,quantity
        )
        assert broken_phones >= 0, f" Broken Phones {broken_phones} is not greater than or equal to zero!"
          
        #assign to self object     
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones 
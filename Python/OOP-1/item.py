import csv

class Item:
    
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        
        #run validations to received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f" Quantity {quantity} is not greater than or equal to zero!"
          
        #assign to self object     
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
         
    def calculate_total_price(self):
        return self.price * self.quantity


     
    @classmethod     
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name =item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),                 
            )
    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        #for i.e 50.0
        
        if isinstance(num, float):
            #Count out the floats that are point zero
            
            return num.is_integer()     
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @property
    def name(self):
        return self.__name
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @name.setter 
    def name(self, value):
        if len > 10:
            raise exceptions("the name is too long")
        else:
            self.__name = value
     
    def apply_increment(self, increment_value):  
        self.__price = self.price + self.price * increment_value 
        
        
    def __repr__(self):
        return f"Item('{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def connect(self, smpt_server):
        pass
    
    def prepare_body(self):
        return f"""
        Hello You.
        We have {self.name} {self.quantity} times.
        Regards, Allen
        """
        
    def send(self):
        pass
    
    def send_email(self):
        self.connect()
        self.prepare_body()
        self.send()
        pass
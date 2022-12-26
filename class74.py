# inheritance
class Phone :
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def full_name(self):
        return f"{self.brand}  {self.model_name}"


    def make_a_call(self,number):
        return f"calling {number}....."

class Smartphone(Phone):#base class / parent class            
    def __init__(self, brand,model_name, price, ram, internal_memory ,rear_camera):
        #two
        # Phone.__init__(self,brand,model_name,price) # uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    # def full_name(self):
    #     return f"{self.brand}  {self.model_name}"
    # def make_a_call(self,number):
    #     return f"calling {number}....."
phone = Phone('nokia','1100',1000)
Smartphone = Smartphone('onePlus','5',30000)
print(phone.full_name())
print(phone.full_name() + f"and price is {Smartphone._price}")


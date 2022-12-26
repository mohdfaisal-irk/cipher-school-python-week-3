class Phone :
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price



 
    def make_a_call(self,phone_number):
       print(f"calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model.name}"


    def send_message(self):
        pass#twilio
phone1 = Phone('Nokia', '1100',1000)
print(phone1.__dict__)
phone2 = Phone('Nokia', '1100',1000)
print(phone2.__dict__)
phone2.__price = -1000
print(phone2.__price)



# l = [3,4,5,6,8] 
# l.sort() #tim sort
# print(l)           
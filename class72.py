# class method as constructor
class Person:
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


@classmethod
def from_string(cls,string):
   first,last,age= string.split('')
   return cls(first,last,age)

@classmethod
def count_instance(cls):
    return f"You have created {cls.count_instance} instances of {cls.__name__}"    

    def is_above_18(self):
        return self.age>18


p1 = Person('Deepa','Das',25)
p2 = Person('Deepa','Das',25)        
p3 = Person.from_string('Deepa','Das',25)    
print(p3.full_name())

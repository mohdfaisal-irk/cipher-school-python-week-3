class Person:
    count_instance = 0
    def __init__(self,first_name, last_name,age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Deepa','Das',25)
p2 = Person('Deepa','Das',25)
p2 = Person('Deepa','Das',25)
p2 = Person('Deepa','Das',25)
print(Person.count_instance)


class Dishes:
    count_instance = 0
    def __init__(self,biryani_chiken, mutton_chiken):
        Dishes.count_instance += 1
        self.biryani_chiken = biryani_chiken        
        self.mutton_chiken = mutton_chiken


D1 = Dishes('dilicious',220)        
D2 = Dishes('dilicious',220)        
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
D2 = Dishes('dilicious',220)    
print(Dishes.count_instance)    



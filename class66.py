# isinstance methode
class Person:
    def __init__(self, first_name,last_name,age):
        self.first_name = first_name
        self.last_age = last_name
        self.age = age
    def full_name(self):
       return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
       return self.age>18

p1 = Person('harshit','vashistha',24)
p2 = Person('harshit','vashistha',24)
# print(p2.full_name)
print(p1.is_above_18)
# Person.full_name(p2)

l = [1,2,3,4]
#clear , pop
# l.clear
list.clear(l)
print(l)
# l.append(10)
list.append(1,10)

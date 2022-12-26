# OBJECTIVES
# WHAT IS class
#HOW TO CREATE AN CLASS
#HOW TO ADD A CLASS
# WHAT IS INIT METHOD, CONSTRUCTOR
# HOW TO CREATE OUR OBJECT

class Person:
     def__init__(self, first_name, last_name, age):
    #  instance variable
    self.person_first_name = first_name
    self.last_name = last_name
    self.age = age
    # instance method

p1 = Person('Harshit', 'Vashistha',24)
# p2 = Person('Mohit','Vashistha',19)

print(p1.person_first_name)
print(p2._person_first_name)


# class variable
# circle
# area
# circum
class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c1 = Circle(4, 3.14)
c2 = Circle(5, 3.14)
print(c2.calc_circumference)

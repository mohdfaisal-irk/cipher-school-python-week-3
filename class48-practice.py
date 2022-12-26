# function returning function to return

def to_power(x):
    def calc_power(n): # n = 2
        return n**x
    return calc_power    

cube = to_power(3)
print(cube(2))


square = to_power(2)
print(cube(2))

square = to_power(2)
print(square(4))


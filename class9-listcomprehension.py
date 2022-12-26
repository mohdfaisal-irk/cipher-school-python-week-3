# we can create a list with only one line
# here were creating a list of cubes 
cubes = []
for i in range(12,25):
    cubes.append(i**3)
print(cubes)  


cube2 = [i**3 for i in  range(12,25)]
print(cube2)

# creating list with all negative values
negative = []
for i in range(25,105):
    negative.append(-i)
print(negative)

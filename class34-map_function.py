# map function
numbers = [22,24,45,60,90]
def cube(a):
    return a**3
cubes = list(map(cube, numbers))
print(cubes)

cubes_new = [i**3 for i in numbers]
print(cubes_new)

new_list= []
for num in numbers:
    new_list.append(cube(num))
print(new_list)    
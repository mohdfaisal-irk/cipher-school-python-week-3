numbers = [20,30,40]  
#  tuples, strings are iterables
cubes = map(lambda a:a**3,numbers)
# iterator
print(cubes)
for i in cubes:
    print(i)
for i in numbers:
    print(numbers)    

# iter function is used to call  
iter(numbers)
next(iter(numbers))
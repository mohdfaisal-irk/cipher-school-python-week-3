def is_even(s):
    return s%2 == 0
numbers = [4,5,6,7,8,9,60,54]   
a = tuple(filter(lambda s:s%2==0,numbers))
print(a)

for i in a:
    print(i)
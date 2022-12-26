x = [1,2,3]
if x :
    print("not empty")
else:
    print("empty")    
def to_power(num, *args):
    if args:
        return [ i**num for i in args]
    else:
        return "You didnt pass any args"
x = [1,2,3]
print(to_power(3, *x))          
def sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
         a = 0
         for num in args:
            a += num
         return a
    else:
        return "Your Input is Wrong"

print(sum(45,64,91))        
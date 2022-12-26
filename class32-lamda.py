# give a input and check if it is odd or not in line 6
def is_odd(a):
    return a %2 == 1

isodd = lambda a : a%2==1 
print(isodd(5))  

# using lambda prinitng the last letter of ant given input
def last_char(s):
    return s[-1]
last_char = lambda s : s[-1]
print(last_char(input()))  

# using if else conditions with lambda
def func(s):
    if len(s) > 10: 
        return  True
    return False
func = lambda s : True if len(s) > 10 else False   
print(func(input()))     
          
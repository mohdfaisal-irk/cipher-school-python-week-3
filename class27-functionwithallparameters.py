# parameters args default prarameters kwargs
def func(name = input(), age = input()):
    print(name)
    print(age)
func(input(), input())
def func(name,*args,last_name = input(), **kwargs):
    print(name)
    print(args)   


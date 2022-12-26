def decorator_function(any_function):
    def wrapper_function():
        print('this is awsome function')
        any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print("this is function with argumrnt")

# func(7) 
@decorator_function
def fun(a):
    print(f'this is function with argument{a}')

@decorators_funtion
def add(a,b):
    return a + b

add(2,3)           
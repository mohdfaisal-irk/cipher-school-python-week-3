def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
        return wrapper 

@print_function_data
def add(a,b):
    '''This function takes two number as argument and returntheir sum'''
    return a+b


print(add(4,5))    
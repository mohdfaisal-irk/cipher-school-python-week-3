def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        print('this is awsome function')
        any_function(*args, **kwargs)
    return wrapper_function


@decorators_funtion
def add(a,b):
    '''this is add function'''
    return a + b

print(add.__doc__)
print(add.__name__)    
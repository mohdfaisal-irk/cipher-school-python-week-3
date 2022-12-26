def multiply_num(num, *args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_num(input()))        
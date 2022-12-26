def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} :{v}")
x = input()
y= input()    
func(first_name = x, last_name = y)    

numbers = [1,2,4,5,7]
print(min(numbers))

def func(item):
    return len(item)

names = ['deepadaaas', 'shree','ab']
# print(max(names, key = func ))
print(max(names,key = lambda item : len(item)))
students = {
    'deepa' : {'score' :90, 'age':24},
    'shree' : {'score' :80, 'age':34},
    'rohit' : {'score' :70, 'age':14}
}

student2 = [
    {'name' : 'deepa', 'score':90, 'age':24},
    {'name' : 'shree', 'score':80, 'age':34},
    {'name' : 'rohit', 'score':70, 'age':14},
]
print(min(student2,key = lambda item:item.get('score'))['name'])
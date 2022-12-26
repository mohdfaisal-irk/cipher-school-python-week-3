# there is no order inside a dictionary one can access it 
# any way
d=input()
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'values2'
print(empty_dict)
# to check the existence we use "check keyword"
for key, value in d.items():
    print(f'key is {keys} and value is {value}')
# to print all the keys    # 
for i in d:
    print(i)

# to delete we use pop
x = d.pop('name')
print(x)



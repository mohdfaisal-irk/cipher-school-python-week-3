x = [1,2,3,4]
y = [6,7,8,9]
a=[]
z = [(1,7), (2,7), (3,8), (4,9)]

x, y = list(zip(*z))
print(list(x))
print(list(y))
for pair in zip(x,y):
    a.append(max(pair))
print(a)    
a= {'name', 'age', 'place'}
x=input()
# check input is present in given set or not
if x in a:
    print('present')
else:
    print('not present')    
#for loop
for item in a:
    print(item)
l = [1,2,3,4]
print(set[1])     
# intersection and union of sets
b={1,2,3,6,8,9}
c={2,4,6,4,5,8,0}
union = b | c
print(union)
print(b&c)


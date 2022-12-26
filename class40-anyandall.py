num1 = [1,2,3,5,6,7,8]
num2 = [1,3,5,7,9,11,13]

odd = []
for num in num1:
    odd.append(num%2==1)

print(odd) 
print(all([num%2--1 for num in num1]))


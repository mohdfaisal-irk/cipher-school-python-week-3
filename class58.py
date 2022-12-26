#create your first generator with generator
# 1.generator function 

# 10,  to 10

def nums(n):
    for i in range(1,n+1):
        yield(i)

for number in nums(10):
    print(number)        

   # memory--------->

numbers = nums(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)    

#memory list
#memory gen
numbers = list(range(20,35))
evem_numbers = [22,24,26]
nums = []
# printing even numbers
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)   
# printing numbers which are not multiples of 5
for i in numbers:
    if i % 5 == 1:
        nums.append(i)
print(numbers)             


nums = [1,12,34,5,67,89,100,1,4,5,6]
new_list = []
# multiples of 4 in given list
for i in nums:
    if i % 4 == 0:
        new_list.append(i*4)
print(new_list)   

new_list2 = [i*4 if (i%4 == 0) else -1 for i in nums]
print(new_list2)

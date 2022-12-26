def avg(x,y):
    average = []
    for pair in zip(x,y):
        average.append(sum(pair)/len(pair))
    return average
 
print(avg([25,26,80],[70,20,45])) 


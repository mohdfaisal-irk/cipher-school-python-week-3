fruits = ['grapes','mango','apple']
# sort
fruits.sort()
print(fruits)

fruits2 = ('grapes','mango','apple')
sorted(fruits)
print(fruits)

fruits3 = {'grapes','mango','apple'}

guitars = [
    {'model' : 'yamaha f310','price':8400},
    {'model' : 'fortuna f310','price':5400},
    {'model' : 'tvs f310','price':9400},
    {'model' : 'supersplender f310','price':6400}
]
sorted_guitars=(sorted(guitars, key = lambda d:d['price'],reverse = True))
print(sorted_guitars)
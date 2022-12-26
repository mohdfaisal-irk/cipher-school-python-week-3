# given list numbers is odd/even
a=[1,2,3,4,5,6,7,8,9,15,16,20,22]
odd_even={i:('even' if i%2==0 else 'odd') for i in range(10,20)}
print(odd_even)
# multiples of 7 or not
x={i:('Is MUltiple of 7' if i%7==0 else 'Not a multiple') for i in range(50,75)}
print(x)
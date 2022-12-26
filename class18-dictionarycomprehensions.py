num = int(input())
square = {f"Sqaure of {num} is ":num**2}
print(square)
for k,v in square.items():
    print(f"{k} : {v}")
a=input()
count = {char:a.count(char) for char in a}
print(count)


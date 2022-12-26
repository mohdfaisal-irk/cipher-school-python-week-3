# using enumerate function for any given input

names = [input(), input(), input()]
pos = 0
for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")

def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return  -1
print(find_pos(names,input()))             
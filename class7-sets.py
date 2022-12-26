s = {1,2,3,4,5,2,1}
# print(s[1])
# removing same numbers or repeated ones
a = list(set(s))
print(a)
s.add(4)
s.add(6)
print(s)
s.remove(4)
print(s)
s.discard(2)
print(s)
s.clear()
print(s)



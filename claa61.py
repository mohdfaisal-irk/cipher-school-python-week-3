import time
# list vs generatorr


t1 = time.time()
for i in range(1000000):
    print(i)
    t2 = time.time()
    if t2 - t1 > 0.1:
        break
    
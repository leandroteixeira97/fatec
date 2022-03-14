import random

v1 = random.sample(range(100), 10)
v2 = random.sample(range(100), 10)
v3 = []

for pos in range(10):
    v3.append(v1[pos])
    v3.append(v2[pos])
           
print(v1)
print(v2)
print(v3)
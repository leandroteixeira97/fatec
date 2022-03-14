import random

v = random.sample(range(100), 20)

par = []
impar = []

for pos in v:
    if (pos % 2) == 0:
        par.append(pos)
    else:
        impar.append(pos)

print(v)
print(par)
print(impar)
import random

v = random.sample(range(100), 10)

max = v[9]
min = v[0]

for pos in v:
    if pos > max:
        max = pos
    if pos < min:
        min = pos

print(v)
print(f'Máximo: {max}\nMínimo: {min}')
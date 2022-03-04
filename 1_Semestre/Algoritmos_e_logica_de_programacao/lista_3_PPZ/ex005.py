n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
rest = 1

while rest > 0:
  n1, n2 = n2, n1 % n2
  rest = n2

print(f'O máximo divisor comum entre os dois números é {n1}')
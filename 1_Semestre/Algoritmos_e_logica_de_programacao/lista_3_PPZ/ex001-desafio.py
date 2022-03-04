n = int(input('Digite um número inteiro não negativo: '))
t1 = 0
t2 = t1 + 1
t3 = t2 + 1
triangular = t1 * t2 * t3

while n > triangular:
  triangular = t1 * t2 * t3
  t1 += 1
  t2 += 1
  t3 += 1

if n == triangular:
  print('Este número é triangular')
else:
  print('Este número não é triangular')
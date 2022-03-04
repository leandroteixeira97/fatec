n = int(input('Digite um número: '))
cont = 1
rest = 1

if n == 1:
  print('Este número não é primo')
elif n ==2:
  print('Este é um número primo')
else:
  while rest != 0:
    cont += 1
    rest = n % cont
  if cont != n:
    print('Este número não é primo')
  else:
    print('Este é um número primo')

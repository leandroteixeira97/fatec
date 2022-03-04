number = int(input('Digite um número inteiro: '))

a = 1
b = 1
c = 0
fibonacci = 0

if number == 1 or number == 2:
    print(f'O correspondente de {number} na sequência de Fibonacci é 1')
else:
    while c < number:
        a, b = b, a + b
        fibonacci = b
        c += 1
    print(f'A posição {number} na sequência de Fibonacci corresponde ao valor {fibonacci}')
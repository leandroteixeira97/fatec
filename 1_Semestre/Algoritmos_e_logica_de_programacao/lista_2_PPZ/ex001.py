a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if (abs(a-b) < c < (a+b)) and (abs(a-c) < b < (a+c)) and (abs(b-c) < a < (b+c)):
    if a==b and b==c:
        print('Este é um triângulo equilátero')
    elif a==b or b==c:
        print('Este é um triângulo isósceles')
    else:
        print('Este é um triângulo escaleno')
else:
    print('Os dados informados não constituem um triângulo possível')

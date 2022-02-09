km = float(input('Qual a quantidade de quilômetros percorridos? '))
days = float(input('Por quantos dias o carro foi alugado? '))

print(f'O preço a pagar é de R$ {((km * 0.15 + 60 * days) ):.2f}')
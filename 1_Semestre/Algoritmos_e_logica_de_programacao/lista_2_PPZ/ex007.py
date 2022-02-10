from math import ceil


paintArea = float(input('Digite em m² a área a ser pintada: '))
inkAmount = ceil(paintArea / 3)

if inkAmount % 18 == 0:
    print(f'Quantidade de latas de tinta a serem compradas: {int(inkAmount / 18)}\nPreço total: R$ {(inkAmount / 18 * 80):.2f}')
else:
    if inkAmount < 18:
        inkAmount = 18
        print(f'Quantidade de latas de tinta a serem compradas: {int(inkAmount / 18)}\nPreço total: R$ {(inkAmount / 18 * 80):.2f}')
    else:
        inkAmount = ceil(inkAmount / 18)
        print(f'Quantidade de latas de tinta a serem compradas: {int(inkAmount)}\nPreço total: R$ {(inkAmount * 80):.2f}')

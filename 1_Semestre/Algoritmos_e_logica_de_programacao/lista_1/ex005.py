productValue = float(input('Digite o valor da mercadoria: '))
discountPercentage = float(input('Digite o percentual de desconto: ')) / 100

print(f'O valor da mercadoria com desconto é de R$ {(productValue * (1 - discountPercentage)):.2f}')
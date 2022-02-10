salary = float(input('Digite o valor do salário: '))
raisePercentage = float(input('Digite a porcentagem do aumento: ')) / 100

print(f'O salário aumentado foi para R$ {(salary * (1 + raisePercentage)):.2f}')
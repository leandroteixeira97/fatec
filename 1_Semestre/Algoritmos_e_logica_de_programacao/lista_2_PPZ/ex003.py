fishWeight = float(input('Digite a quantidade de quilos pescada: '))
weightExcess = fishWeight - 50

if weightExcess <= 0:
    print(f'Quantidade pescada: {fishWeight} kg \nValor do excesso de peso: 0 kg \nValor da multa: R$ 0,00')
else:
    fee = weightExcess * 4
    print(f'Quantidade pescada: {fishWeight} kg \nValor do excesso de peso: {weightExcess} kg \nValor da multa: R$ {fee:.2f}')

distance = float(input('Qual a distância a ser percorrida? (Km) '))
averageSpeed = float(input('Qual a velocidade média esperada para a viagem? (Km/h) '))

travelTime = distance / averageSpeed

print(f'O tempo estimado para a viagem é de aproximadamente {travelTime:.2f} horas')
cigarsPerDay = int(input('Quantos cigarros por dia você fuma? '))
yearsSomoking = int(input('Por quantos anos você já fumou? '))

print(f'Você perdeu {(yearsSomoking * 365 * cigarsPerDay * 10 / 60 / 24):.2f} dias de vida ao fumar')
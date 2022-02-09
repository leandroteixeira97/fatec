days = int(input('Digite a quantidade de dias: ')) * 24 * 60 * 60
hours = int(input('Digite a quantidade de horas: ')) * 60 * 60
minutes = int(input('Digite a quantidade de minutos: ')) * 60
seconds = int(input('Digite a quantidade de segundos: '))

print(f'O total corresponde à {(days + hours + minutes + seconds)} segundos')
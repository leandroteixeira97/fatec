populationA = 80000
populationB = 200000

growthRateA = 0.03
growthRateB = 0.015

years = 0

while populationA <= populationB:
    years += 1
    populationA = populationA + populationA*growthRateA
    populationB = populationB + populationB*growthRateB

print(f'A população do país A ultrapassou o país B\nPopulação do país A: {populationA:.0f}\nPopulação do país B: {populationB:.0f}\nAnos necessários: {years}')
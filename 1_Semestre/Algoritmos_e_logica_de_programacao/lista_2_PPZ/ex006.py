salaryPerHour = float(input('Digite o seu salário por hora: '))
workHours = float(input('Digite a quantidade de horas trabalhadas no mês: '))
netSalary = salaryPerHour * workHours

print(f'Salário Bruto: R$ {netSalary:.2f}\nIR (11%): R$ {(netSalary * 0.11):.2f}\nINSS (8%): R$ {(netSalary * 0.08):.2f}\nSindicato (5%): R$ {(netSalary * 0.05):.2f}\nSalário Liquido: R$ {(netSalary * 0.76):.2f}')
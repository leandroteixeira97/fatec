year = int(input('Digite o ano: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('O ano é bissexto')
        else:
            print('O ano não é bissexto')
    else:
        print('O ano é bissexto')
else:
    print('O ano não é bissexto')

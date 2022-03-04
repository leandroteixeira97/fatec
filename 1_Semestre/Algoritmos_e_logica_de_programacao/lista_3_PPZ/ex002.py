username = input('Digite o nome do usuário: ')
password = input('Digite a senha: ')

while username == password:
    print('ERRO! Usuário deve ser diferente da senha!')
    username = input('Digite o nome do usuário: ')
    password = input('Digite a senha: ')
         
print(f'Usuário: {username}\nSenha: {password}')
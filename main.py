import util as u

print(' ----------- Sistema de gestão de jogadores ----------- ')

sair = 'n'
validar = False

while sair != 's':
    print('1) Cadastrar jogadores')
    print('2) Listar todas os jogadores')
    print('3) Buscar jogadores')
    print('4) Alterar jogadores')
    print('5) Deletar jogadores')
    print('6) Deletar todas as jogadores')

    while validar == False:
        try:
            opc = int(input('Digite a opção desejada: '))
            if opc == 1:
                u.cadastrar()
                validar = True
            elif opc == 2:
                u.listar()
                validar = True
            elif opc == 3:
                u.buscar()
                validar = True
            elif opc == 4:
                u.alterar()
                validar = True
            elif opc == 5:
                u.deletar()
                validar = True
            elif opc == 6:
                u.deleteTodos()
                validar = True
            else:
                print('Número ínvalido.')
                validar = False
        except NameError:
            print('Formato não suportado')
    validar = False

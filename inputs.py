import operator


def flotas(text):
    validacao = True
    while validacao:
        try:
            num = input(text)
            if operator.contains(num, ','):
                print("Use '.' ao invés de ','")
                continue
            num = float(num)
            validacao = False
        except:
            print('Formato não suportado, digite somente números.')
    return num


def ints(text):
    validacao = True
    while validacao:
        try:
            num = input(text)
            if operator.contains(num, ',') or operator.contains(num, '.'):
                print('Digite somente números inteiros.')
                continue
            num = int(num)
            validacao = False
        except:
            print('Formato não suportado, digite somente números.')
    return num


def opcoes(list, text):
    while True:
        if text == '':
            text = 'Digite a opção desejada: '
        opc = input(text)
        if opc in list:
            return opc
        else:
            print('Não é uma opção valida')
            continue

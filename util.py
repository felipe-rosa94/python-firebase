import time as t
import firebase as db
import random as r
import inputs


def cadastrar():
    dados = {}

    nome = input('Digite seu nome: ')
    time = input('Digite seu time: ')

    chave = key()
    dados['key'] = chave
    dados['nome'] = nome
    dados['time'] = time
    dados['data'] = dataHora()

    db.insert('jogadores', chave, dados)


def listar():
    obj = db.getAll('jogadores')
    print('---------- JOGADORES ----------')
    for i in obj:
        print(obj[i]['nome'], ':', obj[i]['time'])
        print('número de registro:', obj[i]['key'])

    print('-------------------------------\n')


def buscar():
    print('como deseja buscar ? ')

    order = inputs.opcoes(['t', 'n', 'r'], 'time (t), nome (n) ?, registro (r) ? ').lower()

    if order == 't':
        equalTo = input('time : ').lower()
        order = 'time'
    elif order == 'n':
        equalTo = input('nome : ').lower()
        order = 'nome'
    elif order == 'r':
        equalTo = input('registro : ').lower()
        order = 'key'
    else:
        print('formato inválido')
        return

    obj = db.equalTo('jogadores', order, equalTo)

    print('---------- JOGADORES ----------')
    for i in obj:
        print(obj[i]['nome'], ':', obj[i]['time'])
        print('número de registro:', obj[i]['key'])

    print('-------------------------------\n')


def alterar():
    key = input('qual número de registro do jogador ? ').lower()

    dados = {}

    nome = input('Digite seu nome: ')
    time = input('Digite seu time: ')

    dados['key'] = key
    dados['nome'] = nome
    dados['time'] = time
    dados['data'] = dataHora()

    db.insert('jogadores', key, dados)


def deletar():
    key = input('qual número de registro do jogador ? ').lower()
    db.remove('jogadores', key)


def deleteTodos():
    db.removeAll('jogadores')


def dataHora():
    data = t.localtime()
    ano = str(data.tm_year)
    mes = str(data.tm_mon)
    dia = str(data.tm_mday)
    hora = str(data.tm_hour)
    minuto = str(data.tm_min)
    segundos = str(data.tm_sec)
    return (ano + '/' + mes + '/' + dia + ' ' + hora + ':' + minuto + ':' + segundos)


def key():
    data = dataHora()
    data = data.replace("/", "")
    data = data.replace(" ", "")
    data = data.replace(":", "")
    return data + '-' + str(r.randint(0, 99))

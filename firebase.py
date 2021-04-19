import pyrebase

config = {
    "apiKey": "AIzaSyDfCCqxjtz59ypRUyxop2fDOrwu5qFr9s0",
    "authDomain": "python-541cc.firebaseapp.com",
    "databaseURL": "https://python-541cc.firebaseio.com",
    "projectId": "python-541cc",
    "storageBucket": "",
    "messagingSenderId": "275978567901",
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


def insert(table, key, obj):
    ##
    # comando push cria uma key automatica
    # database.child(nome da tabela).push(dados)
    #
    #
    # comando update permite criar a key
    # database.child(nome da tabela).chil(coloque a key).push(dados)
    #
    database.child(table).child(key).update(obj)


def getAll(table):
    obj = database.child(table).get()
    return dict(obj.val())


def equalTo(table, orderBy, equalTo):
    obj = database.child(table).order_by_child(orderBy).equal_to(equalTo).get()
    return dict(obj.val())


def removeAll(table):
    database.child(table).remove()


def remove(table, key):
    database.child(table).child(key).remove()

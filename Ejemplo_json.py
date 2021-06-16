import json, csv

'''
class Employee(object):
    def __init__(self, name, work):
        self.name = name
        self.work = work

def jsonDefault(object):
    return object.__dict__

abder = Employee('Abder', 'Programadora')
jsonAbder = json.dumps(abder, default=jsonDefault)

print(jsonAbder)
'''

# funcion para guardar las puntuaciones de los jugadores
def SaveScores(sc, hs, user):
    user = user
    sc = sc
    hs = hs
    lista = []
    with open("puntajeJugadores.csv", newline='') as File:
        reader = csv.reader(File)
        lista.append([user, hs, sc])
        for row in reader:
            if len(row) > 0:
                if user != row[0]:
                    lista.append(row)
                if hs <= int(row[1]) and user == row[0]:
                    exit()
    writer = csv.writer(open('puntajeJugadores.csv', 'w'), delimiter=",")
    writer.writerows(lista)

#SaveScores(1,7,"Ruben")
#SaveScores(2,9,"Monica")
#SaveScores(3,16,"Flor")
#SaveScores(4,32,"Allan")

# funcion para cargar los puntajes más altos de los jugadores
def verpuntaje( user):
    user = user
    nuser = ""
    npuntos = ""
    with open("puntajeJugadores.csv", newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if len(row) > 0:
                if user == row[0]:
                    nuser = row[0]
                    npuntos = row[1]
    print("El puntaje de "+nuser+" es: "+ npuntos)

verpuntaje("Allan")




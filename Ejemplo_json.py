import json, csv

# funcion para guardar las puntuaciones de los jugadores
def guardarPuntaje(sc, hs, user):
    user = user
    sc = sc
    hs = hs
    lista = []
    imprimir = "imprime"
    with open("puntajeJugadores.csv", newline='') as File:
        reader = csv.reader(File)
        lista.append([user, hs, sc])
        for row in reader:
            if len(row) > 0:
                if user != row[0]:
                    lista.append(row)
                    if imprimir == "no":
                        imprimir = "no"
                    else:
                        imprimir = "imprime"
                if hs < int(row[1]) and user == row[0]:
                    imprimir = "no"
    if imprimir == "imprime":
        writer = csv.writer(open('puntajeJugadores.csv', 'w'), delimiter=",")
        writer.writerows(lista)

#guardarPuntaje(1,7,"Ruben")
#guardarPuntaje(2,9,"Monica")
#guardarPuntaje(3,16,"Flor")
#guardarPuntaje(4,32,"Allan")
#guardarPuntaje(5,20,"Kendall")
#guardarPuntaje(6,5,"Pino")
guardarPuntaje(7,64,"Aaron")


# funcion para cargar los puntajes más altos de los jugadores
def verPuntaje( user):
    user = user
    nuser = " "
    npuntos = " "
    with open("puntajeJugadores.csv", newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if len(row) > 0:
                if user == row[0]:
                    nuser = row[0]
                    npuntos = row[1]
    #print("El puntaje de "+nuser+" es: "+ npuntos)

verPuntaje("Allan")
verPuntaje("Flor")

# Creamos la lista de diccionarios
datos = {}
datos["lider"] = []
lista = []
# Abrimos el archivo csv para escribir cada columna de la puntuacion alta en una lista
with open("puntajeJugadores.csv", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        if len(row) > 0 and row[0] != "":
            lista += [(int(row[1]))]
# Ordenamos esa lista de nemor a mayor y la invertimos para obtener la puntuacion mas alta
lista.sort()
lista.reverse()

#print(lista)

# Abrimos el archivo, leemos el jugador y la puntuacion  y lo ingresamos en una lista
puntos = []
with open("puntajeJugadores.csv", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        if len(row) > 0:
            if row[0] != "":
                puntos.append([row[0], row[1]])

print(puntos)

# Recorremos la lista ordenada y la lista desordenada para guardar en una lista de diccionarios la puntuacion mas alta
for lis in lista:
    for row in puntos:
        if len(row) > 0:
            if int(row[1]) == lis:
                datos["lider"].append({"Jugador": row[0], "Puntuacion": row[1]})

print(datos)

# Abrimos el archivo con JSON y escribimos el diccionario
with open("archivojson.json", 'w') as file:
    json.dump(datos["lider"], file)

# Escribimos en las listbox los primeros 5 jugadores con puntuacion alta
with open("archivojson.json") as lider:
    high = json.load(lider)
    contador = 0
    for h in high:
        if contador < 5:
            print(h["Jugador"] + ": Puntuacion ---> " + h["Puntuacion"])
        contador = contador + 1


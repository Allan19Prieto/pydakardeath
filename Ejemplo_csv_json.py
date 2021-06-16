import csv, json

csvFilePath = 'puntajeJugadores.csv'
jsonFilePath = 'archivojson.json'

#Seleen los datos del csv
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['']
        data[id] = rows


#Se crea el archivo  json y se escribe en el
with open(jsonFilePath, 'w') as jsonFile:
    #mas vistoso
    jsonFile.write(json.dumps(data, indent=4))


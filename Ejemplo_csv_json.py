import csv, json

csvFilePath = 'drive_registration.csv'
jsonFilePath = 'driver2.json'

#Seleen los datos del csv
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

#Se crea el archivo  json y se escribe en el
with open(jsonFilePath, 'w') as jsonFile:
    #mas vistoso
    jsonFile.write(json.dumps(data, indent=4))


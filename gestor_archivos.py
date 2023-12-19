import csv

def almacenar_datos(input, puntaje, tiempo):
    with open("puntajes.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([input, puntaje, tiempo])
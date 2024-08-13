'''
    TOMADO DEL CURSO DE COMPREHENSIONS, ESTA ES LA REFERENCIA A DICHO CURSO
    Video 37: http://xatakamovil.com/analisis/realme-c55-analisis-caracteristicas-precio-especificaciones
    Ejemplo de lectura de un csv, vamos a leer el archivo world_population.csv

'''

import csv


def leer_csv(path):
    with open(path, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=',')
        encabezado = next(lector) #leido el archivo toma la primera fila, el encabezado
        arreglo = []
        for fila in lector: 
            # print('***'*5)
            # print(fila) #Estas funciones solo imprime linea por linea asi como viene
            iterable = zip(encabezado, fila) #cada fila la empareja con el header, a modo llave valor
            #print(list(iterable))
            #Sin embargo, hasta a partir de este punto lo haremos un diccionario
            dict_pais = {key: value for  key, value in iterable}
            #print(dict_pais)
            arreglo.append(dict_pais)
        return arreglo

#Nuestra magica linea para que este archivo se ejecute como parte del modulo tanto como de forma individual
if __name__ == '__main__':
    data = leer_csv('./csv_lessons/world_population.csv')
    print(data)
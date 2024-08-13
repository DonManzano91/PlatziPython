'''
    En este archivo manejamos el uso de graficas utilizando la libreria matplotlib:
    https://platzi.com/clases/4260-python-funciones/55088-creando-una-grafica/
'''
import matplotlib.pyplot as ploter
import numpy as np

''' 
    Con la libreria instalada podemos recurrir a varios tipos de grafica basado en las 
    propias reglas de la libreria
'''

def grafica_de_barras(tag, valor):
    ax = ploter.subplot()
    ax.bar(tag, valor)
    ploter.show()

def grafica_de_pie():
    # fig, ax = ploter.subplots()
    # ax.pie(valor, labels=tag)
    # ax.axis('equal')
    valores = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    ploter.pie(valores, labels=mylabels)
    ploter.title("pie simple")
    ploter.show()

if __name__ == '__main__':
    labels = [1, 2, 3] #esto la hace funcionar, debo investigar que pedo
    values = [10, 20, 70]
    opcion = input('marca 1, si quieres graf de b1arras, 2 si la quieres de pie: \n')
    if opcion == '1':
        grafica_de_barras(labels, values)
    elif opcion == '2':
        grafica_de_pie()
    else:
        print('Es grafica de barras o de pie, no hay de otra prro')
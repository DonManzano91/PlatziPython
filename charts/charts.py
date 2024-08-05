import matplotlib.pyplot as pylot

def generar_grafica_pie():
    labels=['A', 'B', 'C']
    values = [200, 100, 20]

    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig('pie.png')
    pylot.close()
    print("Funcion generar_grafica_pie() ejecutada correctamente")
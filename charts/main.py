#archivo que implementa la logica de ejecucion una ves se ejecuta el proyecto
#Statement que importa librerias:
import charts

#statement que define como se ejecutaran los paquetes asociados a este proyecto
def run():
    charts.generar_grafica_pie()

'''
sentencia para definir si va standalone o parte de un proyecto las instrucciones
aca dejadas:
'''
if __name__ == '__main__':
    run()
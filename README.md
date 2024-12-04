Esta carpeta se estara ejecutando para llevar a cabo el curso

Python: PIP y Entornos Virtuales

Aqui no se pueden añadir imagenes, asi que dependiendo lo que necesite guardar
habra de utilizarse una serie de anotaciones en Notion que estaran mutuamente
enlazados, de mientras, vamos a trabajar con puro texto a ver que tal, mas que
mada para mantener este tipo de cursos como algo un poco mas practico que teo-
rico.

Notas Generales:

Bloque 1: Introducción
    En Este no hay mucho que decir, es una serie de videos ayudando a setear un
    entorno de trabajo, seteo de WSL, git, Github, VSCode, Python3. Mucha de esta
    informacion ha sido revisada en otros cursos de mucha ayuda sin tanta bronca
    
Bloque 2: PIP y Entornos Virtuales
    Aqui empieza la carnita de este curso, vamos a empezar a interactuar con los 
    entornos mas profesionales del desarrollo en Python.

    V7: https://platzi.com/home/clases/4261-python-pip/55127-que-es-pip/
        ¿Que es PIP? al parecer dentro de python es la estructura de librearias que 
        utiliza em si el lenguaje, digamos que es el simil a maven de Java.
        
        Parece que dentro de la estrucutra del curso vamos a utilizar proyectos 
        anidados, por lo cual se genera una diferente carpeta "charts"

        comandos usados:
        $pip3 -V
        $pip3 install <nombre del paquete o dependencia que quermos jalar>
            Este comando baja las dependencias a nivel OS, no aparecera nada a nivel
            de la carpeta donde se este utilizando este proyecto
        $pip3 freeze
            Nos da el panorama completo de dependencias descargadas al entorno de 
            desarrollo
        
        Se generaron archivos para ejemplificar el uso de estas librerias:
            charts/main.py
            charts/charts.py

    V8: https://platzi.com/home/clases/4261-python-pip/55128-graficas-en-python-con-pip/
        Vamos a utilizar el proyecto CSV para generar graficas, parece que fue usado en
        el curso de comprehension, pero, se añade tambien la referencia de este lado, se
        usara de forma independendiente en este proyecto.
        
        Estos nuevos archivos se estan añadiendo en los directorios /app para referencia
        de uso.

    V9: https://platzi.com/home/clases/4261-python-pip/55129-que-es-un-ambiente-virtual/
        Python esta instalado en el entorno general de la compu, junto con todas sus dependencias
        de forma que si se instalan proyectos varios en la maquina, todo esta disponible
        para todos, lo cual puede ser problematico a nivel microservicios.

        Supongo en este punto sera de revisar empaquetamientos de dependencias, el equivalente
        a gradle/maven en java.

        

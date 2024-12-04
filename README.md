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

        De aca la importancia de mantener empaquetados diferentes de cada proyecto con sus
        respectivas dependencias, de esta forma manejaremos los ambientes virtuales por cada uno 
        de los proyectos

    V10: 
        Comandos ejecutados:
        $which python3 -> Nos dice donde esta alojado el ejecutor que usara el entorno virtual que usaremos.

        $which pip3 -> Lo mismo pero para el gestor de dependencias.

        $sudo apt install -y python3-venv -> Instalación del manejador de entornos virtuales, con este podremos
                                             crearlos y (supongo) configurarlos. Este comando es usado por 
                                             sistemas basados en debian, en mac no hace falta instalar este 
                                             gestor, ya que viene en la instalacion por default de homebrew

        $ python3 -m venv nombreDelAmbiente -> crea el directorio de ambiente virtual dentro del cual existiran
                                               los comandos para activar y desactivar el entorno acorde sea 
                                               necesario 

        $source nombreDelAmbiente/bin/activate -> Activa el entorno virtual de modo que toda instalacion o gestion 
                                    de dependencia se hara dentro de ese entorno, este se ejecuta dentro de la 
                                    carpeta, que sera destinada a ser un entorno (o en este caso, dentro de cada 
                                    proyecto).

        $deactivate -> Nos saca del entorno virtual que antes ya habriamos accedido, de nuevo este se ejecuta cuando
                       estemos dentro del proyecto particular que hayamos usado.

    V11:
        Igual que con java y sus archivos para maven o gradle, en python se usa un archivo llamado requirements.txt
        como gestor de dependencias.

        Se proporcionan la documentacion necesaria para poder ejecutar el proyecto cuando uno es nuevo en dicho
        proyecto.

        Para llenar el requirements.txt se usa el siguiente comando con base en las dependencias alguna vez generadas
        para poder usar el proyecto:

        $ pip3 freeze > requirements.txt

Bloque 3: Practicas

Aca empieza un segmento bien bonito he interesante para hacer o entender como fucionan ciertos marcos de trabajo con 
python.
    V12:
        En este caso se utilizara la libreria request para mandar un request a una API y manejar su respuesta dentro 
        de un nuevo proyecto.
        Libreria: https://requests.readthedocs.io/en/latest/
        APi Fake: https://fakeapi.platzi.com

        se ejecutan las instrucciones de V10 para crear el ambiente virtual de este nuevo proyecto.
        Directorio con archivos propios creados para esta clase estan en /web-server
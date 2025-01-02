import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return[1,2,3]

@app.get("/nombre", response_class=HTMLResponse)
def get_nombre():
    return '''
    <html>
        <head>
            <title>Respuesta en HTML</title>
        </head>
        <body>
            <h1>Asi es, respuesta en html</h1>
        </body>
    </html>
    '''
def run():
    store.get_categorias()

if __name__ == '__main__':
    run()
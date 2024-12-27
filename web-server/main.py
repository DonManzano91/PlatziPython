import store
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return[1,2,3]

@app.get("/nombre")
def get_nombre():
    return{"nombre" : "alejandro"}

def run():
    store.get_categorias()

if __name__ == '__main__':
    run()
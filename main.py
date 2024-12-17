from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hola": "Mundo",
        "Hello":"World"
        }

        # Tipos de parametros de rutas


#       de Rutas  "/"
@app.get("/items/{item_id}")
def read_id(item_id: int, q: Union[str, None] = None ):
    return {'item_id :': item_id, "q:":q }  


#       de Consulta "?","&"
@app.get("/calculadora")
def calcular(operando_1:float, operando_2:float):
    return {'suma: ':operando_1 + operando_2}

'''
Para acceder a la DOCUMENTACION INTERACTIVA: http://127.0.0.1:4007/docs

'''


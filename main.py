from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    
    price: float
    
    is_offer: Union[bool, None]= None
    
    

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
Para acceder a la "Documentacion Interactiva" : http://127.0.0.1:4007/docs

'''


from datetime import date
from pydantic import BaseModel

class cliente(BaseModel):

    nombre: str
    identificacion: str
    fechaNacimiento: date
    sexo: str



class ClientesResponse(BaseModel):
    nombre: str = None
    identificacion: str = None
    fechaNacimiento: date
    sexo: str = None

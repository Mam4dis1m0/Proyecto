from datetime import date
from pydantic import BaseModel, field_validator
from typing import List
from numpy import mean

class cliente(BaseModel):

    nombre: str
    identificacion: str
    fechaNacimiento: date
    fechaIngreso: date
    sexo: str



class ClientesResponse(BaseModel):
    nombre: str = None
    identificacion: str = None
    fechaNacimiento: date
    sexo: str = None

from pydantic import BaseModel


class Producto(BaseModel):
    NombProd: str
    producto: str


class ProductoResponse(BaseModel):
   producto:str
   nombre : str
from pydantic import BaseModel


class Producto(BaseModel):
    id_Cliente: int
    producto: str


class ProductoResponse(BaseModel):
   producto:str
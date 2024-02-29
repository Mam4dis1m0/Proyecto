from fastapi import APIRouter
from BLL.ClienteService import  ClienteService
from Entity.Cliente import cliente

router = APIRouter()
clientedatos = ClienteService()


@router.get("/obtener_todos")
def obtener_todos(cliente):
    return clientedatos.obtener_todos(cliente)


@router.get("/obtener_por_nombre")
def obtener_por_nombre(nombre):
    return clientedatos.obtener_todos(nombre)


@router.post("/guardar_Cliente")
def guardar_cliente(datos: cliente):
    return clientedatos.guardar_cliente(datos)


@router.get("/filtrar_por identificación")
def filtrar(Identificacion: float):
    return Identificacion

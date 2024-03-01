from fastapi import APIRouter
from BLL.ClienteService import  ClienteService
from Entity.Cliente import cliente
from Entity.Cliente import cliente
from BLL.producto import ProductoResponse



clientedatos = ClienteService()
producto= ProductoResponse()
router = APIRouter()


@router.get("/obtener_todos")
def obtener_todos():
    return


@router.get("/obtener_por_cliente")
def obtener_por_cliente(cliente):
    return clientedatos.obtener_todos(cliente)


@router.post("/guardar_Cliente")
def guardar_cliente(datos: cliente):
    return clientedatos.guardar_cliente(datos)


@router.get("/filtrar_por identificación")
def filtrar(Identificacion: float):
    return Identificacion , guardar_cliente

@router.post("/productoResponse")
def guardar_producto(informacion: producto, id: int):
    return producto.registrar_producto(informacion, id)

@router.get("/Consultar_clientes_por_Producto")
def Cliente_producto():
    return cliente.filtrar_cliente_producto()
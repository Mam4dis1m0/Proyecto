from BLL.connection_manager import ConnectionManager
from DAL.Prouctos_repository import ProductoResponse


class ProductoResponse():
    __connection_manager = ConnectionManager()
    __producto_service = ProductoResponse(__connection_manager.get_connection())
    def registrar_producto(self, datos_producto , id):
        self.__connection_manager.open_connection()
        self.__producto_service.guardar_producto(datos_producto, id)
        self.__connection_manager.close_connection()
        return "Se registro Correctamente el producto!"
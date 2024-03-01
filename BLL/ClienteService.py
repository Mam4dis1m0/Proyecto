from DAL.Clientes_repository import ClientesRepository
from BLL.connection_manager import ConnectionManager

class ClienteService():

    __connection_manager = ConnectionManager()
    __Clientes_repository = ClientesRepository(__connection_manager.get_connection())

    def obtener_todos(self):
        self.__connection_manager.open_connection()
        clientes = self.__Clientes_repository.obtener_todos()
        self.__connection_manager.close_connection()
        return clientes

    def guardar_cliente(self, clientes):
        self.__connection_manager.open_connection()
        self.__Clientes_repository.guardar_cliente(clientes)
        self.__connection_manager.close_connection()
        return "El Cliente sido  registrado con éxito."

    def filtrar_por_identificación(self ,clientes):
        self.__connection_manager.open_connection()
        self.__Clientes_repository.guardar_cliente(clientes)
        self.__connection_manager.close_connection()
        return clientes

    def consultar_cliente(self):
        self.__connection_manager.open_connection()
        consul_cliente = self.__Clientes_repository.guardar_cliente()
        self.__connection_manager.close_connection()
        return consul_cliente


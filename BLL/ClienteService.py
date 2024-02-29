from DAL.Clientes_repository import ClientesRepository
from BLL.connection_manager import ConnectionManager

class ClienteService():

    __connection_manager = ConnectionManager()
    __Clientes_repository = ClientesRepository(__connection_manager.get_connection())

    def obtener_todos(self):
        self.__connection_manager.open_connection()
        Cliente = self.__Clientes_repository.obtener_todos()
        self.__connection_manager.close_connection()
        return Cliente

    def guardar_cliente(self, Cliente):
        self.__connection_manager.open_connection()
        self.__Clientes_repository.guardar_cliente(Cliente)
        self.__connection_manager.close_connection()
        return "El Cliente sido  registrado con éxito."

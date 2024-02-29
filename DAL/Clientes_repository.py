from mysql.connector.abstracts import MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection

from Entity.Cliente import cliente, ClientesResponse
from Entity.producto import Producto


class ClientesRepository():
    def __init__(self, connection):
        self.connection = connection

    def obtener_cliente(self):
        return self.__cliente

    def obtener_todos(self):
        cliente = []
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT nombre,sexo ,Identificacion ,Fecha_Nacimiento)"
            "FROM `clientes`.e "
            "LEFT JOIN `productos`.n "
            "ON e.id_cliente = n.id "
        )
        result = cursor.fetchall()
        for item in result:
            cliente.append(self.mapear_Clientes(item))

        cursor.close()
        return cliente

    def guardar_cliente(self,cliente:cliente):

        id = None
        cursor = self.connection.cursor()

        sql = ("INSERT INTO cliente(nombre , sexo , Identificacion,Fecha_Nacimiento) "
               "VALUES(%s, %s, %s, %s)")

        values = (
           cliente.identificacion,
           cliente.nombre,
           cliente.sexo,
            str(cliente.fechaNacimiento))



    def guardar_producto(self, producto):
        cursor = self.connection.cursor()

        sql = ("INSERT INTO producto(id_cliente, producto) "
               "VALUES(%s, %s)")

        values = (
            (producto[0].id_cliente, producto[0].producto),
        )

        cursor.executemany(sql, values)
        self.connection.commit()
        cursor.close()



    def mapear_Clientes(self, registro):
        return ClientesResponse(
            identificacion=registro[0],
            nombre=registro[1],
            sexo=registro[2],
            fechaNacimiento=registro[3]
        )
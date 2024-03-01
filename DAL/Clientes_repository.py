from Entity.Cliente import cliente, ClientesResponse
from Entity.producto import Producto,ProductoResponse


class ClientesRepository():
    def __init__(self, connection):
        self.connection = connection

    def TD_cliente(self):
        return self.__Clientes

    def obtener_todos(self):
        Datos = []
        cursor = self.connection.cursor()
        cursor.execute(

            'SELECT  nombre , sexo ,  Identificacion ,   Fecha_Nacimiento )' 
            
            'FROM clientes e'
            
            'LEFT JOIN productos n '
            
            'ON e.id = n.id_cliente '

        )

        result = cursor.fetchall()
        for item in result:
            Datos.append(self.mapear(item))

        cursor.close()
        return Datos

    def guardar_cliente(self, Cliente: cliente):
        cursor = self.connection.cursor()
        sql = ("INSERT INTO Cliente(nombre , sexo , Identificacion,Fecha_Nacimiento) "
               "values(%s,%s,%s,%s)")

        values = (
           cliente.identificacion,
           cliente.nombre,
           cliente.sexo,
            str(cliente.fechaNacimiento))


        cursor.execute(sql, values)
        self.connetion.commit()
        cursor.close()



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





def mapear( self, registro):
    nombre, apellido, identificacion, sexo, fecha_nacimiento, valor_producto, nombre_producto = registro
    return ClientesResponse(
        nombre=nombre,
        apellido=apellido,
        identificacion=identificacion,
        sexo=sexo,
        fecha_nacimiento=fecha_nacimiento,
        ProductoResponse=ProductoResponse(
            nombre_producto=str(nombre_producto),
            valor=int(valor_producto)
        )
    )
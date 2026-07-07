from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                producto.mostrar_informacion()
                return
        print("Producto no encontrado.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                cliente.mostrar_informacion()
                return
        print("Cliente no encontrado.")
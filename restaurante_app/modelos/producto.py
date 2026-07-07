# Clase que representa un producto del restaurante

class Producto:

    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip() == "":
            raise ValueError("Debe ingresar el nombre del producto.")
        self._nombre = nombre

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria.strip() == "":
            raise ValueError("Debe ingresar una categoría.")
        self._categoria = categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible

    def mostrar_informacion(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "No disponible"

        print("\n========== PRODUCTO ==========")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Estado: {estado}")
        print("==============================")
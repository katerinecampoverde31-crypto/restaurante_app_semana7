# Programa principal

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu():
    print("\n==============================")
    print(" SISTEMA DEL RESTAURANTE ")
    print("==============================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("7. Salir")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            disponible = input("¿Disponible? (si/no): ").lower() == "si"

            try:
                producto = Producto(nombre, categoria, precio, disponible)
                restaurante.registrar_producto(producto)
                print("Producto registrado correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            restaurante.listar_productos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            restaurante.buscar_producto(nombre)

        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            cedula = input("Cédula: ")
            correo = input("Correo: ")

            try:
                cliente = Cliente(nombre, cedula, correo)
                restaurante.registrar_cliente(cliente)
                print("Cliente registrado correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            cedula = input("Ingrese la cédula del cliente: ")
            restaurante.buscar_cliente(cedula)

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
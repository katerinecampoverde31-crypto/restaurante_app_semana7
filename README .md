# Sistema de Restaurante

**Estudiante:** Josselyn Katerine Campoverde Encarnación

## Descripción

En este proyecto desarrollé un sistema para administrar un restaurante utilizando Python y Programación Orientada a Objetos. El programa permite registrar, listar y buscar productos y clientes mediante un menú interactivo que funciona desde la consola.

## Estructura del proyecto

- modelos
  - producto.py
  - cliente.py
- servicios
  - restaurante.py
- main.py
- README.md

## Clase Producto

La clase `Producto` utiliza el constructor `__init__` para crear los objetos con su nombre, categoría, precio y disponibilidad. También se aplican `@property` y `@setter` para validar la información antes de guardarla.

## Clase Cliente

La clase `Cliente` fue creada utilizando `@dataclass`, lo que permite organizar mejor los datos y facilita la creación de los objetos.

## Clase Restaurante

La clase `Restaurante` se encarga de administrar las listas de productos y clientes. Además, contiene los métodos para registrar, listar y buscar la información ingresada por el usuario.

## Menú interactivo

El programa se ejecuta desde el archivo `main.py`. El menú permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del sistema.

Todos los datos son ingresados por el usuario mediante la función `input()`.

## Reflexión

Con este proyecto reforcé los conocimientos adquiridos en clase sobre Programación Orientada a Objetos. Aprendí a trabajar con clases, constructores, propiedades, `@dataclass` y a organizar un programa en diferentes módulos, logrando un código más claro y fácil de mantener.
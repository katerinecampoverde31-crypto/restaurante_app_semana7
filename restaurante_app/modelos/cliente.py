# Clase Cliente usando dataclass

from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    cedula: str
    correo: str

    def __post_init__(self):
        if self.nombre.strip() == "":
            raise ValueError("Debe ingresar el nombre del cliente.")

        if self.cedula.strip() == "":
            raise ValueError("Debe ingresar la cédula.")

        if self.correo.strip() == "":
            raise ValueError("Debe ingresar el correo.")

    def mostrar_informacion(self):
        print("\n========== CLIENTE ==========")
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Correo: {self.correo}")
        print("=============================")
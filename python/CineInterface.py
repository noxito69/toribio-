import json
from cine import Cine
from prettytable import PrettyTable
from sala import Sala
from funcion import Funcion
from FuncionInterface import FuncionInterface
from SalaInterface import SalaInterface

class CineInterface:
    def __init__(self, cines, salas, funciones):
        self.cines = cines
        self.salas = salas
        self.funciones = funciones

    def ver_cines(self):
        table = PrettyTable(["ID", "Nombre", "Dirección", "Estado", "Tipo Cine", "Número de Salas"])

        for index, cine in enumerate(self.cines.arreglo):
            table.add_row([index + 1, cine.nombre, cine.direccion, cine.estado, cine.tipoCine, cine.numeroSalas])

        print(table)

    def agregar_cine(self):
        nombre = input("Ingrese el nombre del cine: ")
        direccion = input("Ingrese la dirección del cine: ")
        estado = input("Ingrese el estado del cine: ")
        tipo_cine = input("Ingrese el tipo de cine: ")
        numero_salas = int(input("Ingrese el número de salas del cine: "))

        nueva_cine = Cine(nombre, direccion, estado, tipo_cine, numero_salas)

        # Pass the existing Sala and Funcion instances from the new Cine object
        sala_interface = SalaInterface(nueva_cine.sala, self.funciones)
        sala_interface.menu_principal()

        # Add the cine to the array
        self.cines.post(nueva_cine)

        # Save changes in the JSON file after adding cine, salas, and functions
        self.guardar_en_archivo()
        print("Cine agregado con salas y funciones correctamente.")

        return nueva_cine

    def editar_cine(self):
        self.ver_cines()
        index = int(input("Ingrese el índice del cine a editar: ")) - 1

        if self.index_exist(index):
            nuevo_nombre = input(f"Ingrese el nuevo nombre ({self.cines.arreglo[index].nombre}): ")
            nueva_direccion = input(f"Ingrese la nueva dirección ({self.cines.arreglo[index].direccion}): ")
            nuevo_estado = input(f"Ingrese el nuevo estado ({self.cines.arreglo[index].estado}): ")
            nuevo_tipo_cine = input(f"Ingrese el nuevo tipo de cine ({self.cines.arreglo[index].tipoCine}): ")
            nuevo_numero_salas = int(input(f"Ingrese el nuevo número de salas ({self.cines.arreglo[index].numeroSalas}): "))

            self.cines.arreglo[index].nombre = nuevo_nombre
            self.cines.arreglo[index].direccion = nueva_direccion
            self.cines.arreglo[index].estado = nuevo_estado
            self.cines.arreglo[index].tipoCine = nuevo_tipo_cine
            self.cines.arreglo[index].numeroSalas = nuevo_numero_salas

            self.cines.ConvertoJson()
            print("Cine editado con éxito.")

            # Preguntar si desea editar salas y funciones
            editar_salas = input("¿Desea editar las salas y funciones de este cine? (s/n): ").lower()

            if editar_salas == "s":
                # Obtener las salas del cine actual
                salas_cine = self.cines.arreglo[index].sala

                # Crear una SalaInterface para gestionar las salas y funciones de este cine
                sala_interface = SalaInterface(salas_cine, self.funciones)
                sala_interface.menu_principal()

        else:
            print("Índice no válido.")

    def eliminar_cine(self):
        self.ver_cines()
        index = int(input("Ingrese el índice del cine a eliminar: ")) - 1

        if self.index_exist(index):
            cine_eliminado = self.cines.arreglo.pop(index)
            self.cines.ConvertoJson()
            print(f"Cine eliminado con éxito: {cine_eliminado.nombre}")
        else:
            print("Índice no válido.")

    def guardar_en_archivo(self):
        self.cines.ConvertoJson()
        print("Datos guardados en el archivo cines.json")

    def index_exist(self, index):
        return 0 <= index < len(self.cines.arreglo)

    def menu_principal(self):
        while True:
            print("\n--- Interfaz Cines ---")
            print("1. Ver cines")
            print("2. Agregar cine")
            print("3. Editar cine")
            print("4. Eliminar cine")
            print("5. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.ver_cines()
            elif opcion == 2:
                self.agregar_cine()
            elif opcion == 3:
                self.editar_cine()
            elif opcion == 4:
                self.eliminar_cine()
            elif opcion == 5:
                self.guardar_en_archivo()  # Añadir esta línea al salir del bucle
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    cines = Cine()
    cines.extract(cines.extraer_json("cines"))

    salas = Sala()
    salas.extract(salas.extraer_json("salas"))

    funciones = Funcion()
    funciones.extract_funciones(funciones.extraer_json("funciones"))

    cine_interface = CineInterface(cines, salas, funciones)
    cine_interface.menu_principal()

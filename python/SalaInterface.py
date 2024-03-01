import json
from prettytable import PrettyTable
from sala import Sala
from funcion import Funcion
from FuncionInterface import FuncionInterface

class SalaInterface:
    def __init__(self, salas, funciones):
        self.salas = salas
        self.funciones = funciones

    def ver_salas(self):
        table = PrettyTable(["ID", "Número Sala", "Capacidad", "Proyector", "Audio", "Tipo Sala"])

        for index, sala in enumerate(self.salas.arreglo):
            table.add_row([index + 1, sala.numero_sala, sala.capacidad, sala.proyector, sala.audio, sala.tipo])

        print(table)

    def agregar_sala(self):
        numero_sala = int(input("Ingrese el número de sala: "))
        capacidad = int(input("Ingrese la capacidad de la sala: "))
        proyector = input("Ingrese el tipo de proyector: ")
        audio = input("Ingrese el tipo de audio: ")
        tipo = input("Ingrese el tipo de sala: ")

        nueva_sala = Sala(numero_sala, capacidad, proyector, audio, tipo)

        # Create a FuncionInterface for managing functions for this sala
        funcion_interface = FuncionInterface(Funcion(), f"sala_{numero_sala}")
        funcion_interface.menu_principal()

        # Get the functions from the FuncionInterface and assign them to the sala
        nuevas_funciones = funcion_interface.funciones.arreglo.copy()
        nueva_sala.funciones = nuevas_funciones

        # Add the sala to the array
        self.salas.post(nueva_sala)

        # Save changes in the JSON file after adding sala and functions
        self.guardar_en_archivo()
        print("Sala agregada con funciones correctamente.")

    def editar_sala(self):
        self.ver_salas()
        index = int(input("Ingrese el índice de la sala a editar: ")) - 1

        if self.index_exist(index):
            nueva_capacidad = input(f"Ingrese la nueva capacidad ({self.salas.arreglo[index].capacidad}): ")
            nuevo_proyector = input(f"Ingrese el nuevo tipo de proyector ({self.salas.arreglo[index].proyector}): ")
            nuevo_audio = input(f"Ingrese el nuevo tipo de audio ({self.salas.arreglo[index].audio}): ")
            nuevo_tipo = input(f"Ingrese el nuevo tipo de sala ({self.salas.arreglo[index].tipo}): ")

            self.salas.arreglo[index].capacidad = nueva_capacidad
            self.salas.arreglo[index].proyector = nuevo_proyector
            self.salas.arreglo[index].audio = nuevo_audio
            self.salas.arreglo[index].tipo = nuevo_tipo

            self.salas.ConvertoJson()
            print("Sala editada con éxito.")

            # Preguntar si desea editar funciones
            editar_funciones = input("¿Desea editar las funciones de esta sala? (s/n): ").lower()

            if editar_funciones == "s":
                # Obtener las funciones de la sala actual
                funciones_sala = self.salas.arreglo[index].funcion

                # Crear una FuncionInterface para gestionar las funciones de esta sala
                funcion_interface = FuncionInterface(funciones_sala, f"sala_{self.salas.arreglo[index].numero_sala}")
                funcion_interface.menu_principal()

        else:
            print("Índice no válido.")

    def eliminar_sala(self):
        self.ver_salas()
        index = int(input("Ingrese el índice de la sala a eliminar: ")) - 1

        if self.index_exist(index):
            sala_eliminada = self.salas.arreglo.pop(index)
            self.salas.ConvertoJson()
            print(f"Sala eliminada con éxito: Sala {sala_eliminada.numero_sala}")
        else:
            print("Índice no válido.")

    def guardar_en_archivo(self):
        self.salas.ConvertoJson()
        print("Datos guardados en el archivo salas.json")

    def index_exist(self, index):
        return 0 <= index < len(self.salas.arreglo)

    def menu_principal(self):
        while True:
            print("\n--- Interfaz Salas ---")
            print("1. Ver salas")
            print("2. Agregar sala")
            print("3. Editar sala")
            print("4. Eliminar sala")
            print("5. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.ver_salas()
            elif opcion == 2:
                self.agregar_sala()
            elif opcion == 3:
                self.editar_sala()
            elif opcion == 4:
                self.eliminar_sala()
            elif opcion == 5:
                self.guardar_en_archivo()  # Añadir esta línea al salir del bucle
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    salas = Sala()
    salas.extract(salas.extraer_json("salas"))

    funciones = Funcion()
    funciones.extract_funciones(funciones.extraer_json("funciones"))

    sala_interface = SalaInterface(salas, funciones)
    sala_interface.menu_principal()

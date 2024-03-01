import json
from prettytable import PrettyTable
from funcion import Funcion

class FuncionInterface:
    def __init__(self, funciones, archivo):
        self.funciones = funciones
        self.archivo = archivo

    def ver_funciones(self):
        table = PrettyTable(["ID", "Nombre Película", "Hora", "Sala", "Precio", "Duración", "Género"])

        for index, funcion in enumerate(self.funciones.arreglo):
            funcion.id = index + 1
            table.add_row([funcion.id, funcion.nombre_pelicula, funcion.hora_funcion, funcion.sala,
                           funcion.precio, funcion.duracion, funcion.genero])

        print(table)

    def agregar_funcion(self):
        nombre = input("Ingrese el nombre de la película: ")
        hora = input("Ingrese la hora de la función: ")
        sala = int(input("Ingrese el número de sala: "))
        precio = float(input("Ingrese el precio: "))
        duracion = int(input("Ingrese la duración en minutos: "))
        genero = input("Ingrese el género de la película: ")

        nueva_funcion = Funcion(nombre, hora, sala, precio, duracion, genero)
        self.funciones.post(nueva_funcion)
        print("Función agregada con éxito.")

     
        if self.archivo == "funciones":
            self.guardar_en_archivo()

        # Return the newly added function for the calling class to handle
        return nueva_funcion

    def modificar(self):
        self.ver_funciones()
        index = int(input("Ingrese el índice de la función a modificar: ")) - 1  # Ajustar el índice

        if self.index_exist(index):
            nueva_funcion = input(f"Ingrese la nueva función ({self.funciones.arreglo[index].nombre_pelicula}): ")
            nueva_hora = input(f"Ingrese la nueva hora ({self.funciones.arreglo[index].hora_funcion}): ")
            nuevo_sala = input(f"Ingrese el nuevo número de sala ({self.funciones.arreglo[index].sala}): ")
            nuevo_precio = input(f"Ingrese el nuevo precio ({self.funciones.arreglo[index].precio}): ")
            nueva_duracion = input(f"Ingrese la nueva duración en minutos ({self.funciones.arreglo[index].duracion}): ")
            nuevo_genero = input(f"Ingrese el nuevo género de la película ({self.funciones.arreglo[index].genero}): ")

            self.funciones.arreglo[index].nombre_pelicula = nueva_funcion
            self.funciones.arreglo[index].hora_funcion = nueva_hora
            self.funciones.arreglo[index].sala = nuevo_sala
            self.funciones.arreglo[index].precio = nuevo_precio
            self.funciones.arreglo[index].duracion = nueva_duracion
            self.funciones.arreglo[index].genero = nuevo_genero

            self.funciones.ConvertoJson()
            print("Función modificada con éxito.")
        else:
            print("Índice no válido.")

    def eliminar(self):
        self.ver_funciones()
        index = int(input("Ingrese el índice de la función a eliminar: ")) - 1  # Ajustar el índice

        if self.index_exist(index):
            funcion_eliminada = self.funciones.arreglo.pop(index)
            self.funciones.ConvertoJson()
            print(f"Función eliminada con éxito: {funcion_eliminada.nombre_pelicula}")
        else:
            print("Índice no válido.")

    def guardar_en_archivo(self):
        self.funciones.ConvertoJson()
        print("Datos guardados en el archivo funciones.json")

    def index_exist(self, index):
        return 0 <= index < len(self.funciones.arreglo)

    def menu_principal(self):
        while True:
            print("\n--- Interfaz Funciones ---")
            print("1. Ver funciones")
            print("2. Agregar función")
            print("3. Modificar función")
            print("4. Eliminar función")
            print("5. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.ver_funciones()
            elif opcion == 2:
                self.agregar_funcion()
            elif opcion == 3:
                self.modificar()
            elif opcion == 4:
                self.eliminar()
            elif opcion == 5:
                break
            else:
                print("Invalida")

if __name__ == "__main__":
    funciones = Funcion()
    funciones.extract_funciones(funciones.extraer_json("funciones"))

    funcion_interface = FuncionInterface(funciones, "funciones")
    funcion_interface.menu_principal()
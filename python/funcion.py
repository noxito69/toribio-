from arreglo import Arreglo
import json
class Funcion(Arreglo):
    
    def __init__(self, nombre_pelicula=None, hora_funcion=None, sala=None, precio=None, duracion=None, genero=None):
        self.nombre_pelicula = nombre_pelicula
        self.hora_funcion = hora_funcion
        self.sala = sala
        self.precio = precio
        self.duracion = duracion
        self.genero = genero    
        super().__init__()
        
    def __str__(self) -> str:
        return f"{self.nombre_pelicula} ({self.hora_funcion}) (Sala {self.sala}) (Precio: ${self.precio}) (Duración: {self.duracion} minutos) (Género: {self.genero})"
        
    def dictionary(self):
        return{
            
            "nombre_pelicula": self.nombre_pelicula,
            "hora_funcion":self.hora_funcion,
            "sala":self.sala,
            "precio":self.precio,
            "duracion":self.duracion,
            "genero":self.genero
            
        }
        
    def ConvertoJson(x):
        funciones = [x.dictionary()for x in x.arreglo]
        with open("./funciones.json", "w") as archivo:
            archivo.write(json.dumps(funciones, indent=2))
            
            
    def extract_funciones(self, json):
        funciones_str = ""
        for funcion in json:
            func = Funcion(funcion['nombre_pelicula'], funcion['hora_funcion'], funcion['sala'], funcion['precio'], funcion['duracion'],funcion['genero'])
            funciones_str += str(func) + "\n"
            self.post(func)
        
        return funciones_str.strip()



             
    
if __name__ == "__main__":
    x = Funcion()
    
    print(x.extract_funciones(x.extraer_json("funciones")))

    for func in x.arreglo:
        print("Funcion", type(func))

    
    
    """
    F = Funcion("SAW", "2:30 PM", 2, 80, 169, "Horror")
    F2 = Funcion("Interestellar", "6:30 PM", 1, 80, 169, "Ciencia ficcion")
    F3 = Funcion("Avengers", "2:30 PM", 2, 80, 169, "Fantasia")
    F4 = Funcion("hello kitty", "5:30 PM", 3, 80, 149, "infantil")
    instancia_funcion = Funcion.from_json("funciones")
    
    x.post(F)
    
    x.post(F2)
    
    x.post(F3)
    
    x.post(F4)
    
    print(x.ConvertoJson())
    print(instancia_funcion.get())  
"""
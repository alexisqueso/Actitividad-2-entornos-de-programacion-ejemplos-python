class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  
        self._edad = edad      

    def hacer_sonido(self):
        pass  

    def describir(self):
        print(f"Soy {self._nombre}, tengo {self._edad} años.")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau! Guau!")  

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau! Miau!") 

mi_perro = Perro("Fido", 3)
mi_gato = Gato("Misu", 2)

mi_perro.describir()    
mi_perro.hacer_sonido() 

mi_gato.describir()     
mi_gato.hacer_sonido() 
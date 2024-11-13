# Definir la clase Libro
class Libro:
    # Constructor para inicializar los atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
    
    # Método para mostrar la información del libro
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

# Crear un objeto de la clase Libro
mi_libro = Libro("Cócora", "Ricardo Puello")

# Llamar al método para mostrar la información del libro
mi_libro.mostrar_info()

# Función para ingresar una lista de valores desde el usuario
def ingresar_lista():
    numeros = []  # Inicializar una lista vacía para almacenar los valores
    print("Ingresa los valores para la lista (escribe 'fin' para terminar):")
    while True:
        # Pedir un valor al usuario
        valor = input("Ingresa un valor: ")
        # Salir del bucle si el usuario escribe "fin"
        if valor.lower() == 'fin':
            break
        try:
            # Intentar convertir el valor a un número (int o float)
            numero = float(valor) if '.' in valor else int(valor)
            # Agregar el número a la lista si la conversión es exitosa
            numeros.append(numero)
        except ValueError:
            # Si el valor no es numérico, se guarda como texto para manejarlo después
            numeros.append(valor)
    return numeros  # Devolver la lista de valores ingresados

# Función para procesar los números en la lista
def procesar_numeros(numeros, divisor):
    try:
        # Paso 1: Filtrar solo los valores que son números positivos (int o float)
        positivos = list(filter(lambda x: isinstance(x, (int, float)) and x > 0, numeros))
        
        # Verificar si la lista de números positivos está vacía
        if not positivos:
            raise ValueError("La lista no contiene números positivos.")
        
        # Paso 2: Calcular el cuadrado de cada número positivo
        cuadrados = list(map(lambda x: x ** 2, positivos))
        
        # Paso 3: Intentar dividir cada número cuadrado por el divisor dado
        resultados = list(map(lambda x: x / divisor, cuadrados))
        
        return resultados  # Devolver la lista de resultados

    except ZeroDivisionError:
        # Manejar el error si el divisor es cero
        print("Error: El divisor no puede ser cero.")
        return []
    except ValueError as ve:
        # Manejar error si la lista no contiene números positivos
        print(f"Error: {ve}")
        return []
    except TypeError:
        # Manejar error si la lista contiene valores no numéricos
        print("Error: La lista contiene valores no numéricos.")
        return []
    except Exception as e:
        # Manejar otros errores inesperados
        print(f"Error inesperado: {e}")
        return []

# Solicitar al usuario la lista de números
numeros = ingresar_lista()

# Pedir el divisor al usuario y manejar el caso en que no sea un número
try:
    divisor = float(input("Ingresa el divisor: "))
except ValueError:
    # Si el divisor no es válido, asignar un valor predeterminado (1) y notificar al usuario
    print("Error: El divisor debe ser un número.")
    divisor = 1

# Llamar a la función para procesar los números y mostrar los resultados
resultado = procesar_numeros(numeros, divisor)
print("Resultados:", resultado)

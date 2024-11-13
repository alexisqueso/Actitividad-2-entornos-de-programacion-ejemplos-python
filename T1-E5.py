# Función para agregar productos al carrito
def agregar_producto(carrito):
    # Bucle para agregar varios productos hasta que el usuario decida terminar
    while True:
        try:
            # Pedir al usuario el nombre del producto
            nombre = input("Ingresa el nombre del producto (o escribe 'fin' para terminar): ")
            # Si el usuario escribe "fin", salir del bucle
            if nombre.lower() == 'fin':
                break

            # Pedir la cantidad del producto y verificar que sea un número entero positivo
            cantidad = int(input("Ingresa la cantidad de '{}': ".format(nombre)))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")

            # Pedir el precio del producto y verificar que sea un número positivo
            precio = float(input("Ingresa el precio unitario de '{}': ".format(nombre)))
            if precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
            
            # Agregar el producto al carrito como un diccionario con nombre, cantidad y precio
            carrito.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
        
        # Captura errores específicos como valores inválidos y pide ingresar los datos nuevamente
        except ValueError as ve:
            print(f"Error: {ve}. Por favor, ingresa los valores nuevamente.")
        # Captura otros errores inesperados
        except Exception as e:
            print(f"Error inesperado: {e}. Inténtalo nuevamente.")

# Función para calcular el total de la compra
def calcular_total(carrito):
    try:
        # Verificar si el carrito está vacío, en cuyo caso no se puede calcular el total
        if not carrito:
            raise ValueError("El carrito está vacío. No se puede calcular el total.")
        
        # Sumar el subtotal de cada producto en el carrito (cantidad * precio) para obtener el total
        total = sum(item["cantidad"] * item["precio"] for item in carrito)
        return total

    # Captura errores en caso de datos no válidos en el carrito
    except TypeError:
        print("Error: El carrito contiene datos no válidos.")
        return 0
    # Captura otros errores inesperados
    except Exception as e:
        print(f"Error inesperado al calcular el total: {e}")
        return 0

# Función para mostrar el detalle de la compra y el total a pagar
def mostrar_detalle(carrito, total):
    print("\nDetalle de la compra:")
    # Imprimir detalles de cada producto en el carrito
    for item in carrito:
        print(f"{item['nombre']} - Cantidad: {item['cantidad']}, Precio Unitario: {item['precio']:.2f}, Subtotal: {item['cantidad'] * item['precio']:.2f}")
    # Imprimir el total final
    print(f"Total a pagar: {total:.2f}")

# Programa principal
carrito = []  # Inicializar el carrito como una lista vacía
print("Bienvenido al sistema de compras")

# Llamar a la función para agregar productos al carrito
agregar_producto(carrito)

# Calcular el total de la compra
total = calcular_total(carrito)

# Mostrar el detalle de la compra y el total si el total es mayor que cero
if total > 0:
    mostrar_detalle(carrito, total)
else:
    print("No se pudo completar la compra.")

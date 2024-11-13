#programa para gestionar un inventario de ferreteria s
def agregar_producto(inventario):
    try: 
        producto = input ("\nIngrese el nombre del producto: ")
        cantidad = int (input("\nIngrese la cantidad del producto: "))
        
        if producto in inventario:
            inventario[producto] += cantidad

        else: inventario[producto] = cantidad
        
        print (f"Producto '{producto}' agredado exitosamente")
    # Manejo de excepción cuando se ingresa una cantidad no válida
    except ValueError:
        print ("Error: Debes ingrear un número entero para la cantidad.")
    # Manejo de cualquier otro tipo de error inesperado
    except Exception:
        print ("Ha ocurrido un error inesperado.")
        pass #Utilizamos "pass" para omitir el menejo especifico y continuar
    
#Iventario inicial vacio.
inventario = {}

#Bucle principal del programa.
while True:
    try:
        print ("\n                                           GESTION DE INVENTARIO                        ")
        print("\nOpciones: \n1.Agregar Producto \n2.Ver Inventario \n3.Salir")
        opcion = int (input ("Selecciona una opcion: "))

        if opcion == 1:
            agregar_producto (inventario)

        elif opcion == 2:
            print("\nInventario actual:")
            for producto, cantidad in inventario.items():
                print (f"{producto}: {cantidad} unidades")
        
        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else: 
            print ("Error: Opcion no valida. Intentelo de nuevo.")

    except ValueError:
        print ("Error: Debes ingresar un numero entero para seleccionar una opcion.")            
    except Exception:
        print ("Ha ocurrido un error inesperado")
        pass
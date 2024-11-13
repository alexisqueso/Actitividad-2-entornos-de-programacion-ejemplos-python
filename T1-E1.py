import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 100
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 10. Intenta adivinarlo.")

    while True:
        intento = input("Ingresa tu número o escribe 'salir' para terminar: ")

        if intento.lower() == 'salir':
            print("Gracias por jugar. ¡Hasta luego!")
            break

        try:
            intento = int(intento)
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Correcto! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

adivina_el_numero()
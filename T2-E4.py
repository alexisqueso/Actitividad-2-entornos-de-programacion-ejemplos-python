class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El café {self.name} ha sido vendido.")
        else:
            print(f"El café {self.name} no está disponible.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.coffees_purchased = []

    def buy_coffee(self, coffee):
        if coffee.check_availability():
            coffee.sell()
            self.coffees_purchased.append(coffee)
        else:
            print(f"Lo siento, el café {coffee.name} no está disponible.")

    def inquire_coffee(self, coffee):
        availability = "disponible" if coffee.check_availability() else "no disponible"
        print(f"El café {coffee.name} está {availability} y cuesta {coffee.get_price()}.")


class Barista:
    def __init__(self, name):
        self.name = name

    def prepare_coffee(self, coffee):
        if coffee.check_availability():
            print(f"El barista {self.name} está preparando el café {coffee.name}.")
        else:
            print(f"El café {coffee.name} no está disponible para preparar.")


class Cafeteria:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_coffee(self, coffee):
        self.inventory.append(coffee)
        print(f"El café {coffee.name} ha sido añadido al inventario.")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la cafetería.")

    def show_available_coffees(self):
        print("Cafés disponibles en la cafetería:")
        for coffee in self.inventory:
            if coffee.check_availability():
                print(f"- {coffee.name} por {coffee.get_price()}")


# Crear instancias de cafés
coffee1 = Coffee("Latte", 3)
coffee2 = Coffee("Cappuccino", 3.5)
coffee3 = Coffee("Espresso", 2.5)

# Crear instancia de cliente
customer1 = Customer("Ruben")

# Crear instancia de barista
barista1 = Barista("Daniela")

# Crear instancia de cafetería y registrar cafés, clientes y baristas
cafeteria = Cafeteria()
cafeteria.add_coffee(coffee1)
cafeteria.add_coffee(coffee2)
cafeteria.add_coffee(coffee3)
cafeteria.register_customer(customer1)

# Mostrar cafés disponibles
cafeteria.show_available_coffees()

# Cliente consulta un café
customer1.inquire_coffee(coffee1)

# Cliente compra un café
customer1.buy_coffee(coffee1)

# Mostrar cafés disponibles nuevamente
cafeteria.show_available_coffees()

# Cliente intenta comprar un café ya vendido
customer1.buy_coffee(coffee1)

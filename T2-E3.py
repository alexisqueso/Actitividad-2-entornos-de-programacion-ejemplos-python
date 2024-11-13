class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Stock actualizado para {self.nombre}. Nuevo stock: {self.stock}")

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Descuento aplicado a {self.nombre}. Nuevo precio: ${self.precio:.2f}")


class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.puntos_fidelidad = 0

    def acumular_puntos(self, monto_compra):
        puntos = int(monto_compra // 10)  # 1 punto por cada $10 gastados
        self.puntos_fidelidad += puntos
        print(f"{self.nombre} ha acumulado {puntos} puntos. Total de puntos: {self.puntos_fidelidad}")

    def canjear_puntos(self, puntos):
        if puntos <= self.puntos_fidelidad:
            self.puntos_fidelidad -= puntos
            descuento = puntos * 0.5  # Cada punto vale $0.50 de descuento
            print(f"{self.nombre} ha canjeado {puntos} puntos por un descuento de ${descuento:.2f}")
            return descuento
        else:
            print(f"{self.nombre} no tiene suficientes puntos para canjear.")
            return 0


class Empleado:
    def __init__(self, id_empleado, nombre, puesto):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto

    def aplicar_oferta(self, producto, porcentaje_descuento):
        producto.aplicar_descuento(porcentaje_descuento)
        print(f"{self.nombre} ha aplicado un {porcentaje_descuento}% de descuento a {producto.nombre}")


class Supermercado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}
        self.clientes = {}
        self.empleados = {}

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto
        print(f"Producto {producto.nombre} agregado al inventario.")

    def registrar_cliente(self, cliente):
        self.clientes[cliente.id_cliente] = cliente
        print(f"Cliente {cliente.nombre} registrado en el sistema.")

    def contratar_empleado(self, empleado):
        self.empleados[empleado.id_empleado] = empleado
        print(f"Empleado {empleado.nombre} contratado como {empleado.puesto}.")

    def realizar_venta(self, id_cliente, codigo_producto, cantidad):
        if id_cliente in self.clientes and codigo_producto in self.productos:
            cliente = self.clientes[id_cliente]
            producto = self.productos[codigo_producto]
            if producto.stock >= cantidad:
                total = producto.precio * cantidad
                producto.actualizar_stock(-cantidad)
                cliente.acumular_puntos(total)
                print(f"Venta realizada: {cantidad} x {producto.nombre} a ${producto.precio:.2f} c/u. Total: ${total:.2f}")
            else:
                print(f"Stock insuficiente para {producto.nombre}. Stock disponible: {producto.stock}")
        else:
            print("Cliente o producto no encontrado.")

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos.values():
            print(f"- {producto.nombre}: ${producto.precio:.2f} (Stock: {producto.stock})")

    def mostrar_clientes(self):
        print(f"Clientes registrados en {self.nombre}:")
        for cliente in self.clientes.values():
            print(f"- {cliente.nombre} (ID: {cliente.id_cliente}, Puntos: {cliente.puntos_fidelidad})")

    def mostrar_empleados(self):
        print(f"Empleados de {self.nombre}:")
        for empleado in self.empleados.values():
            print(f"- {empleado.nombre} (ID: {empleado.id_empleado}, Puesto: {empleado.puesto})")


# Ejemplo de uso

# Crear supermercado
supermercado = Supermercado("Supermercado La Prosperidad")

# Agregar productos
producto1 = Producto("001", "Arroz", 2.5, 100)
producto2 = Producto("002", "Frijoles", 1.8, 50)
producto3 = Producto("003", "Aceite", 3.0, 30)
supermercado.agregar_producto(producto1)
supermercado.agregar_producto(producto2)
supermercado.agregar_producto(producto3)

# Registrar clientes
cliente1 = Cliente("C001", "María López")
cliente2 = Cliente("C002", "Juan Pérez")
supermercado.registrar_cliente(cliente1)
supermercado.registrar_cliente(cliente2)

# Contratar empleados
empleado1 = Empleado("E001", "Ana García", "Cajera")
empleado2 = Empleado("E002", "Carlos Sánchez", "Gerente")
supermercado.contratar_empleado(empleado1)
supermercado.contratar_empleado(empleado2)

# Mostrar inventario
supermercado.mostrar_inventario()

# Realizar ventas
supermercado.realizar_venta("C001", "001", 5)
supermercado.realizar_venta("C002", "003", 2)

# Mostrar clientes y sus puntos
supermercado.mostrar_clientes()

# Aplicar oferta especial
empleado2.aplicar_oferta(producto2, 10)  # 10% de descuento en Frijoles

# Mostrar inventario actualizado
supermercado.mostrar_inventario()

# Cliente canjea puntos por descuento
descuento = cliente1.canjear_puntos(10)  # Canjea 10 puntos
if descuento > 0:
    print(f"{cliente1.nombre} obtiene un descuento de ${descuento:.2f} en su próxima compra.")

# ~ Creamos clase Item
class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

#  ~ Método para consultar los items disponibles
    def consultar(self):
        print (f"{self.nombre}. Precio: {self.precio}. Cant. disponible: {self.cantidad}")
    
# ~ Creamos clase Pedido
class Pedido:
    def __init__(self, numeroPedido):
        self.numeroPedido = numeroPedido
        self.items = [] # ~ Lista almacenar los items de mi pedido

    def sumarItem(self, item):
        self.items.append(item) # ~ Agrega un item al pedido

    def calcularTotal(self):
        return sum(item.precio for item in self.items)

    def boleta(self):
        print(f"Pedido nro. {self.numeroPedido}")
        for item in self.items:
            print(f"- {item}")
            print("---------------------")
            print(f"Total: ${self.calcularTotal()}")
            print("--------¡Gracias por tu compra!----------")
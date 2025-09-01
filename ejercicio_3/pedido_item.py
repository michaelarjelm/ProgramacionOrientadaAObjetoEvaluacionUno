##Crea una clase ítem con nombre, precio y cantidad, y un método subtotal(). 
##Crea una clase Pedido que permita agregar ítems y calcular el total.

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio 
        self.cantidad = cantidad 
    
    def subtotal(self):
         return self.precio * self.cantidad
           
class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f"haz agregado {item.nombre} x {item.cantidad} {item.precio} a tu carrito")
        

    def calculo_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total


mi_pedido = Pedido()

item1 = Item("celular", 100000, 6)
item2 = Item("laptop", 150000, 4)
item3 = Item("tablet", 180000, 8)

mi_pedido.agregar_item(item1)
mi_pedido.agregar_item(item2)
mi_pedido.agregar_item(item3)

mi_pedido.calculo_total()

    
       
       



    


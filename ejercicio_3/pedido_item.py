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
        
    def agregaritem(self, item):
        self.items.append(item)
        print(f"acabas de agregar {item.cantidad} de  {item.nombre} a tu carrito, es valor es de {item.subtotal()}")

        
    def totalpedido(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total



    
       
       



    


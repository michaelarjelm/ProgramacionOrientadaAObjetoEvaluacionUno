# Ejercicio 3 — Pedido e Ítem
# Crea una clase ítem con nombre, precio y cantidad, y un método subtotal(). Crea una clase Pedido
# que permita agregar ítems y calcular el total.


class Pedido:
    def __init__(self):
        self.items = []
    
    
    
    def agregar_item(self,item):
        self.items.append(item)

            
    def calculo_total(self):
        
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

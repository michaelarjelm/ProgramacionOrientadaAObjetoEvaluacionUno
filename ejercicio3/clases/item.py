#creamos la clase Item, con mayuzcula para no tener problemas con el import.
# clases/Pedido.py
from ejercicio3.clases.item import Item

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: Item):
        self.items.append(item)

    def calcular_total(self) -> float:
        return sum(item.subtotal() for item in self.items)  #calcula el total de la compra 

    def mostrar_detalle(self):
        print("Tus productos son:\n") #esto mostrara los items que se tienen 
        for item in self.items:
            print(item)
        print(f"\nEl total de tu compra es:  = ${self.calcular_total():.2f} Gracias por preferirnos ")

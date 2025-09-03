class Carro_compras:
    def __init__(self):
        self.productos = []



    def agregar_producto(self, producto, cantidad):
        for item in self.productos:
            if item[0].nombre == producto.nombre:
                item[1] += cantidad
                print(f"cantidad de {producto.nombre} actualizada a {item[1]} unidades.")
                return

        self.productos.append([producto, cantidad])
        print(f"Se ha agregado {producto.nombre} x {cantidad} al carrito.")



    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito de compras está vacío.")
            return

        print("***Productos adquiridos***: ")
        for item in self.productos:
            producto = item[0]
            cantidad = item[1]
            print(f"- {producto.nombre}: {cantidad} unidad(es)")
            
            
    
    def calcular_total(self):
        
        total = 0
        for item in self.productos:
            producto = item[0]
            cantidad = item[1]
            total += producto.precio * cantidad
        return total 





    def aplicar_descuento(self, porcentaje_descuento):
    
        total_sin_descuento = self.calcular_total()

        if not (0 <= porcentaje_descuento <= 100):
            print("El porcentaje de descuento debe estar entre 0 y 100.")
            return

        descuento = total_sin_descuento * (porcentaje_descuento / 100)
        total_con_descuento = total_sin_descuento - descuento
        
        print(
            f"- El total de la compra es: \n"
            f"- subtotal: ${total_sin_descuento: } \n"
            f"- descuento ({porcentaje_descuento}%): -${round(descuento):} \n"
            f"- monto a pagar: ${round(total_con_descuento):} \n"
            
        )
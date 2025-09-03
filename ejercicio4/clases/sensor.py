class Sensor:
    def __init__(self, nombre):
            self.nombre = nombre
            self.lista_mediciones = []


    def registrar_valores(self):
        while True:
            ingreso_valor = input("Ingrese el valor de la vibración en Hz (decimal): ")

            if "." in ingreso_valor:
                valor = float(ingreso_valor)
                if valor > 0:
                    self.lista_mediciones.append(valor)
                    print("Valor registrado exitosamente")
                    return 
                else:
                    print("Valor no válido, ingrese un número decimal positivo.")
            else:
                print("Valor no válido. Intente nuevamente.")
            

    def mostrar_mediciones(self):
            print(f"Las mediciones registradas son: {self.lista_mediciones}")
    
    
    def promedio(self):
        if len(self.lista_mediciones) == 0:
            return 0
        prom = round(sum(self.lista_mediciones) / len(self.lista_mediciones),2)
        print(f"El promedio de las mediciones es: {prom} Hz")
        return prom


    def maximo(self):
        if self.lista_mediciones:
            valor_maximo = max(self.lista_mediciones)
            print(f"El valor máximo registrado es {valor_maximo} Hz")
            return valor_maximo
            

    def minimo(self):
        if self.lista_mediciones:
            valor_minimo = min(self.lista_mediciones)
            print(f"El valor máximo registrado es {valor_minimo} Hz")
            return valor_minimo
    

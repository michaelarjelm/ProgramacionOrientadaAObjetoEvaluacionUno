# Ejercicio 4 — Sensor y Mediciones
# Crea una clase Sensor con nombre y una lista de mediciones. Agrega métodos para registrar
# valores, obtener promedio, máximo y mínimo.


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


    def promedio(self):
        if len(self.lista_mediciones) == 0:
            return 0
        prom = round(sum(self.lista_mediciones) / len(self.lista_mediciones),2)
        print(f"El promedio de las mediciones es: {prom} Hz")
        return prom

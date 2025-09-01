class Sensor:
    def __init__(self,nombre,valor):
        self.nombre = nombre
        self.valor = valor
        lista=[1000,3000]
        lista.append(self.valor)
        lista.sort()
        maximo = lista[-1]
        minimo = lista[0]
        print(f"el valor maximo es {maximo} el valor minimo es {minimo}")
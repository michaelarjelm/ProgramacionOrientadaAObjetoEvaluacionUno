class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        lista = []
        lista.append(nombre)
        lista.append(sueldo)
        print(f"tenemos un gasto de ${self.sueldo}")

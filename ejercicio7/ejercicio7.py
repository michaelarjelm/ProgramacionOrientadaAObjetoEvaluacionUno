class Contacto :
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        lista = []
        lista.append(self.nombre)
        lista.append(self.telefono)
        lista.append(self.correo)
        for a in lista:
            print (a)
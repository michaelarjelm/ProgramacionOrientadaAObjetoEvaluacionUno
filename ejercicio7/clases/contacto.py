class Contacto:
    def __init__(self, nombre, apellido, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Teléfono: {self.telefono}, Correo: {self.correo}"

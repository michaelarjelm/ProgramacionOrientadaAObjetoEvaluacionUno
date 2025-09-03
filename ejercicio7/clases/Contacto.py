# creamos la clase contacto / nombre, telefono, correo todo como string 
class Contacto:
    def __init__(self, nombre: str, telefono: str, correo: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} - Tel: {self.telefono}, Email: {self.correo}"

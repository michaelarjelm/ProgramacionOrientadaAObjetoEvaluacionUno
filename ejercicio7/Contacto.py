# ejercicio7/Contacto.py
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo or "invalid@email.com" #correo invalido si no se proporciona ninguno
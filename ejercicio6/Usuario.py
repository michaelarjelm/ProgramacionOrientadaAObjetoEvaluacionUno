# ejercicio6/Usuario.py
class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña =contraseña or "por defecto"  # Contraseña por defecto si no se proporciona ninguna
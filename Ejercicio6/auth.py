# Ejercicio 6 — Usuario y Autenticación simple
# Crea una clase Usuario con nombre de usuario y contraseña. Crea una clase Auth que permita
# registrar usuarios y hacer login validando credenciales.

class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña


#Ejercicio 6 — Usuario y Autenticación simple
#Crea una clase Usuario con nombre de usuario y contraseña. 
#Crea una clase Auth que permita registrar usuarios y hacer login validando credenciales.

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

class Autentificacion:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre_usuario, contraseña):
        nuevo_usuario = Usuario(nombre_usuario, contraseña)
        self.usuarios.append(nuevo_usuario)

    def login(self, nombre_usuario, contraseña):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
                return True
        return False

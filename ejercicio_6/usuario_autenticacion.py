##Crea una clase Usuario con nombre de usuario y contraseña. 
##Crea una clase Auth que permita registrar usuarios y hacer login validando credenciales.

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contraseña
class Auth:
    def __init__(self):
        self.usuarios = []
    def registrar(self, nombre_usuario, contraseña):
        nuevo = Usuario(nombre_usuario, contraseña)
        self.usuarios.append(nuevo)
        print(f"El usuario {self.registrar} registrado con exito.")

    def login(self, nombre_usuario, contraseña):
        for u in self.usuarios:
            if u.nombre_usuario == nombre_usuario and u.contraseña == contraseña:
                print("Login exitoso.")
                return True
        print("Credenciales son incorrectas.")
        return False

#Crea una clase Usuario con nombre de usuario y contraseña. Crea una clase Auth que permita registrar usuarios y hacer login validando credenciales.
class Usuario:
    def __init__(self, nombreUsuario, contraseña):
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña

class Auth:
    def __init__(self):
        self.usuarioRegistrados = {}

    def registrar (self, nombreUsuario, contraseña):
        nuevoUsuario = Usuario(nombreUsuario, contraseña)
        self.usuarioRegistrados[nombreUsuario] = nuevoUsuario
        print(f"Has registrado al usuario '{nombreUsuario}' exitosamente")

    def login (self, nombreUsuario, contraseña):
            usuarioLog = self.usuarioRegistrados.get(nombreUsuario)
            if usuarioLog and usuarioLog.contraseña == contraseña:
                print(f"¡Bienvenido {nombreUsuario}! Has iniciado sesión correctamente")
                return True
            else:
                print("Nombre de usuario o contraseña incorrectos")
                return False

class Usuario: # ~ Clase para representar un usuario
    def __init__(self, nombre, contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia
    
class Auth:
    def __init__(self):
        self.usuarios = [] # ~ Lista para almacenar usuarios registrados

    def registrarUsuario(self, nombre, contrasenia):
        nuevoUsuario = Usuario(nombre,contrasenia)
        self.usuarios.append(nuevoUsuario)
        return nuevoUsuario
    
    def autenticarUsuario(self, nombre, contrasenia):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasenia == contrasenia:
                print("¡Usuario autenticado!")   
                return True
            print("¡Usuario o contraseña incorrectos!")
            return False
    
# ~ ayuda esto no es un meme

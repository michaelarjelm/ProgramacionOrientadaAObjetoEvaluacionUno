#Clase usuario

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

class Auth:
    def __init__(self):
        self.usuarios_registrados = {}

    def registrar_usuario(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios_registrados:
            print(f"El usuario '{nombre_usuario}' ya existe.")
            return False
        
        nuevo_usuario = Usuario(nombre_usuario, contraseña)
        self.usuarios_registrados[nombre_usuario] = nuevo_usuario
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        return True

    def login(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[nombre_usuario]
            if usuario.contrasena == contraseña:
                print(f"¡Bienvenido, {nombre_usuario}!.")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
        else:
            print("El nombre de usuario no existe.")
            return False
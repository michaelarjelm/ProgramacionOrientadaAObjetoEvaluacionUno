#Creacion de usuario

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

#Creamos la clase para autentificar

class Auth:
    def __init__(self):
        self.usuarios = []
    
    def registrar_usuario(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                if usuario.contrasena == contrasena:
                    print(f'❌ el usuario con nombre "{nombre_usuario}" ya existe.')
                    return False
        nuevo_usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios.append(nuevo_usuario)
        print(f'Usuario "{nombre_usuario}" registrado con exito.')
        return True
    
    def login(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                if usuario.contrasena == contrasena:
                    print(f'Exitoso inicio de sesion. ¡BIENVENIDO "{nombre_usuario}"!.')
                    return True
                else:
                    print("Contrasena incorrecta.")
                    return False
        print(f'El usuario "{nombre_usuario}" no existe.')
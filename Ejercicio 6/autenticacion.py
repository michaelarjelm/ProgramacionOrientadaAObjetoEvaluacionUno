from usuario import Usuario

class Auth:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios:
            print("Error: El usuario ya existe.")
            return False
        nuevo_usuario = Usuario(nombre_usuario, contraseña)
        self.usuarios[nombre_usuario] = nuevo_usuario
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")
        return True

    def login(self, nombre_usuario, contraseña):
        if nombre_usuario not in self.usuarios:
            print("Error: Usuario no encontrado.")
            return False
        usuario = self.usuarios[nombre_usuario]
        if usuario.contraseña == contraseña:
            print(f"Login exitoso para el usuario '{nombre_usuario}'.")
            return True
        else:
            print("Error: Contraseña incorrecta.")
            return False

from Ejercicio6.Usuario import Usuario

class Auth:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar_usuario(self, nombre, contraseña):
        nuevo_usuario = Usuario(nombre, contraseña)
        self.usuarios_registrados.append(nuevo_usuario)
        print(f"Usuario '{nombre}' registrado con éxito.")

    def login(self, nombre, contraseña):
        for usuario in self.usuarios_registrados:
            if usuario.nombre == nombre and usuario.contraseña == contraseña:
                print(f"Bienvenido, {nombre}!")
                return True
        print("Credenciales incorrectas.")
        return False 
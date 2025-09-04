# ejercicio6/Auth.py
class Auth:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        for u in self.usuarios: #u será cada usuario en la lista
            if u.nombre == usuario.nombre:
                print("Error: Usuario ya existe.")
                return
        self.usuarios.append(usuario)

    def login(self, nombre, contraseña):
        for u in self.usuarios: #u será cada usuario en la lista
            if u.nombre == nombre and u.contraseña == contraseña:
                return True
        return False
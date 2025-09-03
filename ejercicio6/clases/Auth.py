# creamos la clase Auth, definimos registrar.

from ejercicio6.clases.Usuario import Usuario

class Auth:
    def __init__(self):
        self.usuarios = []

    def registrar(self, username: str, password: str) -> bool:
        # Revisar si ya existe el Usuario 
        for u in self.usuarios:
            if u.username == username:
                return False   # no se pudo registrar el usuario 
        nuevo = Usuario(username, password)
        self.usuarios.append(nuevo)
        return True

    def login(self, username: str, password: str) -> bool:
        for u in self.usuarios:
            if u.username == username and u.validar_password(password):
                return True
        return False

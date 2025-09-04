# Ejercicio 6 — Usuario y Autenticación simple 
# Crea una clase Usuario con nombre de usuario y contraseña. Crea una clase Auth que permita 
# registrar usuarios y hacer login validando credenciales. 

from usuario import Usuario

class Auth:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, username, password):
        
        for u in self.usuarios:
            if u.username.lower() == username.lower():
                print(f" El usuario '{username}' ya existe.")
                return False

        nuevo_usuario = Usuario(username, password)
        self.usuarios.append(nuevo_usuario)
        print(f" Usuario '{username}' registrado correctamente.")
        return True

    def login(self, username, password):
        for u in self.usuarios:
            if u.username.lower() == username.lower() and u.password == password:
                print(f" Login exitoso. Bienvenido, {username}!")
                return True
        print(" Usuario o contraseña incorrectos.")
        return False

    def listar_usuarios(self):
        if not self.usuarios:
            print(" No hay usuarios registrados.")
        else:
            print("\n--- Usuarios registrados ---")
            for u in self.usuarios:
                print(u)

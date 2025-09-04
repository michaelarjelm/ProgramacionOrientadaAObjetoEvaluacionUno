#Crea una clase Auth que permita registrar usuarios y hacer login validando credenciales.
#  
from .usuario import Usuario

class Auth: 
    def __init__(self): 
        self.usuarios = {}

    def registrar(self, username, password): 
        if username in self.usuarios: 
            print("El nombre de usuario ya existe.") 
            return False 
        self.usuarios[username] = Usuario(username, password) 
        print(f"Usuario '{username}' registrado exitosamente.") 
        return True 

    def login(self, username, password): 
        usuario = self.usuarios.get(username) 
        if usuario and usuario.password == password: 
            print(f"Login exitoso. Bienvenido/a, {username}!") 
            return True 
        print("Credenciales inválidas.") 
        return False
    
# Crea una clase Usuario con nombre de usuario y contraseña.
class Usuario:  
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Usuario: {self.username}"



    


class Usuario:
    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        self.contraseña=contraseña

    def __str__(self):
        return f"Usuario:{self.usuario}"




        
#  creamos la clase usuario/ con Usuario y un passwor y definimos la validadcion de la password 

class Usuario:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validar_password(self, password: str) -> bool:
        return self.password == password

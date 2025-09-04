from  ejercicio6.Clases.usuario import Usuario


class Auth:
    def __init__(self):
        self.usuarios = []


    
    def registrar(self,usuario,contraseña):
        usuario = Usuario(usuario,contraseña)
        self.usuarios.append(usuario)
        print("Usuario registrado")
                

    def login(self,usuario,contraseña):
        for self in self.usuarios:
            if self.usuario == usuario and self.contraseña == contraseña:
                print(f"Login correcto:{usuario}")
                return True
            print("Login incorrecto")
        return False





        
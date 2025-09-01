class Usuario:
    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        lista=[]
        lista.append(self.usuario)
        lista.append(self.contraseña)
        for a in lista:
            print(a)
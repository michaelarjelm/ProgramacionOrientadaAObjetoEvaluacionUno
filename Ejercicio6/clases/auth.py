class Auth:
    def __init__(self):
        self.usuarios = []
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print('\nUsuario registrado con exito')
               
    def login(self, usuario, contraseña):
        if self.usuarios:
            if usuario in self.usuarios:
                if usuario.contraseña == contraseña:
                    print(f"\nUsuario '{usuario.nombre}' logueado")
                else:
                    print("\nContraseña invalida")
            else:
                print("\nUsuario no registrado")
        else:
            print('\nNo hay registro de usuarios')




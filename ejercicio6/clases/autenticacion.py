from ejercicio6.clases.usuario import Usuario


class Auth:
    def __init__(self):
        self.usuarios = []
    
    def registrar_usuario(self):
        
        nom_usuario = input("Ingresa el nombre del usuario a registrar: ")
        contraseña = input("Ingresa tu contraseña: ")
        
        
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nom_usuario:
                print(f"El usuario {nom_usuario} ya se encuentra registrado")
                return False

        nuevo_usuario = Usuario(nom_usuario, contraseña)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario '{nom_usuario}' registrado exitosamente.")
        return True
        
        
        
    def login(self):
        if not self.usuarios:
            print("No hay usuarios registrados. Por favor, crea una cuenta.")
            return

        intentos = 3

        while intentos > 0:
            nom_usuario = input("Bienvenido. Ingresa tu nombre de usuario: ")
            contraseña = input("Ingresa tu contraseña: ")
            
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario.nombre_usuario == nom_usuario:
                    usuario_encontrado = usuario
                    break
            
            if usuario_encontrado:
                if usuario_encontrado.contraseña == contraseña:
                    print(f"Bienvenido {nom_usuario}")
                    return
                else:
                    print("Contraseña incorrecta, intenta nuevamente.")
                    intentos -= 1
            else:
                print("Usuario no encontrado, intenta nuevamente.")
                intentos -= 1

        print("Has excedido el número de intentos. Intenta más tarde.")
    

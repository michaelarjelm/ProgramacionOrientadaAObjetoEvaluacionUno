class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"


class Auth:
    def __init__(self):
        self.usuarios = {}  # diccionario para almacenar usuarios registrados

    def registrar(self, nombre_usuario, contrasena):
        # Verificamos si el usuario ya existe
        if nombre_usuario in self.usuarios:
            print(f"El nombre de usuario {nombre_usuario} ya está en uso.")
            return False
        
        # Validamos la longitud de la contraseña
        if len(contrasena) < 6:
            print("La contraseña debe tener al menos 6 caracteres.")
            return False

        nuevo_usuario = Usuario(nombre_usuario, contrasena)
        self.usuarios[nombre_usuario] = nuevo_usuario
        print(f"Usuario {nombre_usuario} registrado exitosamente.")
        return True

    def login(self, nombre_usuario, contrasena):
        usuario_guardado = self.usuarios.get(nombre_usuario)

        if usuario_guardado and usuario_guardado.contrasena == contrasena:
            print(f"Bienvenido, {nombre_usuario}")
            return True
        else:
            print("Credenciales inválidas. Acceso denegado.")
            return False



def main():
    sistema_auth = Auth()

    # Registro de usuarios
    sistema_auth.registrar("usuario1", "contrasena123")
    sistema_auth.registrar("usuario2", "pass456")
    sistema_auth.registrar("usuario1", "otra_contrasena")  # Intento de registro con usuario existente
    sistema_auth.registrar("usuario3", "123")  # Contraseña demasiado corta

    print("\n--- Intentos de Login ---")

    # Intentos de inicio de sesión
    sistema_auth.login("usuario1", "contrasena123")  # Login exitoso
    sistema_auth.login("usuario2", "pass456")        # Login exitoso
    sistema_auth.login("usuario2", "incorrecta")     # Contraseña incorrecta
    sistema_auth.login("usuario4", "cualquiercosa")  # Usuario no existente

if __name__ == "__main__":
    main()

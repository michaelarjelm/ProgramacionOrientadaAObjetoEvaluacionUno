class Usuario:
    """Representa un usuario con nombre y contraseña."""
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
class Auth:
    """Gestiona el registro y la autenticación de usuarios."""
    def __init__(self):
        self.usuarios = {}  # Usamos un diccionario para un acceso rápido por nombre de usuario
    def registrar_usuario(self, nombre_usuario, contraseña):
        """
        Registra un nuevo usuario si el nombre de usuario no existe.
        Devuelve True si el registro fue exitoso, False si ya existe.
        """
        if nombre_usuario in self.usuarios:
            print(f"❌ Error: El nombre de usuario '{nombre_usuario}' ya existe.")
            return False
        nuevo_usuario = Usuario(nombre_usuario, contraseña)
        self.usuarios[nombre_usuario] = nuevo_usuario
        print(f"✅ Usuario '{nombre_usuario}' registrado exitosamente.")
        return True
    def login(self, nombre_usuario, contraseña):
        """
        Intenta iniciar sesión validando las credenciales.
        Devuelve True si el login es exitoso, False en caso contrario.
        """
        if nombre_usuario not in self.usuarios:
            print(f"❌ Error: El nombre de usuario '{nombre_usuario}' no existe.")
            return False
        usuario_existente = self.usuarios[nombre_usuario]
        if usuario_existente.contraseña == contraseña:
            print(f"✅ ¡Bienvenido, '{nombre_usuario}'! Sesión iniciada con éxito.")
            return True
        else:
            print(f"❌ Error: Contraseña incorrecta para el usuario '{nombre_usuario}'.")
            return False
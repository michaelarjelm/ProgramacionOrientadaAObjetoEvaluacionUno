#Clase Auth
from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio6.Clases import Usuario


class Auth:
    def __init__(self):
        self.usuarios_existentes = []
        
    def registro_usuario(self, nombredeusuario, contraseña):
        usuario = Usuario(nombredeusuario, contraseña)
        self.usuarios_existentes.append(usuario)
        print(f"Usuario {nombredeusuario} se ha cargado correctamente")
        
    def acceso(self, nombredeusuario, contraseña):
        for usuario in self.usuarios_existentes:
            if usuario.nombredeusuario == nombredeusuario and usuario.contraseña == contraseña:
                return f"Bienvenido, {nombredeusuario}"
        return "Datos incorrectos"

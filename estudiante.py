from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre, curso, carnet, carrera):
        super().__init__(nombre, curso)
        self.carnet = carnet
        self.carrera = carrera
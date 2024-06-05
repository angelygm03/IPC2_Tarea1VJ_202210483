from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, curso, codigo, profesion):
        super().__init__(nombre, curso)
        self.codigo = codigo
        self.profesion = profesion
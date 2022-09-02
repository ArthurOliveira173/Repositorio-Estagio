from enum import Enum

class CursoHorarioEnum(Enum):
    MANHA = 1
    TARDE = 2
    NOITE = 3
    INTEGRAL = 4

    #Imprime o nome e valor do tipo cursoHorario
    def __str__(self):
        return f'{self.name.lower()}({self.value})'

    #Testa a igualdade entre 2 horarios de curso
    def __eq__(self, outro):
        if isinstance(outro, int):
            return self.value == outro

        if isinstance(outro, CursoHorarioEnum):
            return self is outro

        return False
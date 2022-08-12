from enum import Enum
class MoniTutoEnum(Enum):
    MONITOR = 1
    TUTOR = 2

    #Imprime o nome e valor do tipo monitor/tutor
    def __str__(self):
        return f'{self.name.lower()}({self.value})'

    #Testa a igualdade entre 2 monitores/tutores
    def __eq__(self, outro):
        if isinstance(outro, int):
            return self.value == outro

        if isinstance(outro, MoniTutoEnum):
            return self is outro

        return False
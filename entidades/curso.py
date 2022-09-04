from enums.cursoHorarioEnum import CursoHorarioEnum

class Curso:

    def __init__(self, id, nome, quant_periodos, horario):
        self._id = id
        self._nome = nome
        self._quant_periodos = quant_periodos
        self._horario = CursoHorarioEnum(horario)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def quant_periodos(self):
        return self._quant_periodos

    @quant_periodos.setter
    def quant_periodos(self, quant_periodos):
        self._quant_periodos = quant_periodos

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, horario):
        if horario == 1 or horario == 2:
            self._horario = CursoHorarioEnum(horario)
        else:
            print("Valor de horário inválido")

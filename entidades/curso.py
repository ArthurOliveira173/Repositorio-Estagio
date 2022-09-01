class Curso:

    def __init__(self, id, nome, quant_periodos):
        self._id = id
        self._nome = nome
        self._quant_periodos = quant_periodos

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

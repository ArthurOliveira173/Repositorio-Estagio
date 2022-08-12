from usuario import Usuario
from enums.moniTutoEnum import MoniTutoEnum

class MonitorTutor(Usuario):
    def __init__(self, id, nome, cpf, email, telefone, matricula, curso, periodo, tipo):
        super().__init__(id, nome, cpf, email, telefone)
        self._matricula = matricula
        self._curso = curso
        self._periodo = periodo
        self._tipo = MoniTutoEnum(tipo)

    #Getters & Setters
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if tipo == 1 or tipo == 2:
            self._tipo = MoniTutoEnum(tipo)
        else:
            print("Valor de tipo inválido")
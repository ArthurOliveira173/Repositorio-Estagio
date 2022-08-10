from usuario import Usuario

class AlunoPCD(Usuario):
    def __init__(self, id, nome, cpf, email, telefone, matricula, curso, disciplinas, periodo, deficiencia, data_nascimento):
        Usuario.__init__(self, id, nome, cpf, email, telefone)
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = disciplinas
        self.periodo = periodo
        self.deficiencia = deficiencia
        self.data_nascimento = data_nascimento

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
    def disciplinas(self):
        return self._disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas):
        self._disciplinas = disciplinas

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo

    @property
    def deficiencia(self):
        return self._deficiencia

    @deficiencia.setter
    def deficiencia(self, deficiencia):
        self._deficiencia = deficiencia

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def criarAlunoPCD(self, id, nome, cpf, email, telefone, matricula, curso,
                      disciplinas, periodo, deficiencia, data_nascimento):

        aluno = AlunoPCD(id, nome, cpf, email, telefone, matricula, curso,
                      disciplinas, periodo, deficiencia, data_nascimento)

        return aluno

a = AlunoPCD.criarAlunoPCD(AlunoPCD, 2, "sasd", "sasd", "sasd", "sasd", "sasd", "sasd", "sasd", "sasd", "sasd", "sasd")
print(a.deficiencia)
print(a.id)
print(a.nome)
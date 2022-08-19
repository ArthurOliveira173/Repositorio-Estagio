from entidades.usuario import Usuario


class AlunoPcd(Usuario):
    _alunos = []
    def __init__(self, id, nome, cpf, email, telefone, matricula, curso, disciplinas, periodo, deficiencia, data_nascimento):
        super().__init__(id, nome, cpf, email, telefone)
        self._matricula = matricula
        self._curso = curso
        self._disciplinas = disciplinas
        self._periodo = periodo
        self._deficiencia = deficiencia
        self._data_nascimento = data_nascimento

    #Getters & Setters

    def getAlunosLista(self):
        lista = self._alunos[:]
        return lista

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

    def CriarAlunoPcd(id, nome, cpf, email, telefone, matricula, curso, disciplinas, periodo, deficiencia, data_nascimento):
        aluno = AlunoPcd(id, nome, cpf, email, telefone, matricula, curso, disciplinas, periodo, deficiencia, data_nascimento)
        AlunoPcd._alunos.append(aluno)
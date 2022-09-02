class Acompanhamento():
    _acompanhamentos = []
    def __init__(self, id, semestre, aluno_pcd, monitor, tutor):
        self._id = id
        self._semestre = semestre
        self._aluno_pcd = aluno_pcd
        self._monitor = monitor
        self._tutor = tutor

    #Getters & Setters

    def getAcompanhamentosLista(self):
        lista = self._acompanhamentos[:]
        return lista

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, semestre):
        self._semestre = semestre

    @property
    def aluno_pcd(self):
        return self._aluno_pcd

    @aluno_pcd.setter
    def aluno_pcd(self, aluno_pcd):
        self._aluno_pcd = aluno_pcd

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def tutor(self):
        return self._tutor

    @tutor.setter
    def tutor(self, tutor):
        self._tutor = tutor
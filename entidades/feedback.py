class Feedback:
    _feedbacks = []
    def __init__(self, id, titulo, descricao, data):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._data = data

    #Getters & Setters
    def getFeedbackLista(self):
        lista = self._feedbacks[:]
        return lista
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
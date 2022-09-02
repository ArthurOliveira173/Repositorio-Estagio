
class Monitorias:
    _monitorias = []

    def __init__(self, id, data_inicio, data_fim, id_monitor, id_acompanhamento):
        self._id = id
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._id_monitor = id_monitor
        self._id_acompanhamento = id_acompanhamento

    def getListaMonitorias(self):
        lista = self._monitorias[:]
        return lista
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self._data_inicio = data_inicio

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_inicio(self, data_fim):
        self._data_fim = data_fim

    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_tutor(self, id_monitor):
        self._id_monitor = id_monitor

    @property
    def id_acompanhamento(self):
        return self._id_acompanhamento

    @id_acompanhamento.setter
    def id_acompanhamento(self, id_acompanhamento):
        self._id_acompanhamento = id_acompanhamento
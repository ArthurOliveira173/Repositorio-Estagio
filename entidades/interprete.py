from entidades.usuario import Usuario

class AlunoPcd(Usuario):
    _interpretes = []
    def __init__(self, id, nome, cpf, sexo, email, telefone):
        super().__init__(id, nome, cpf, sexo, email, telefone)

    def getInterpretesLista(self):
        lista = self._interpretes[:]
        return lista
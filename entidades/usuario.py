class Usuario:
    lista = []
    def __init__(self):
        pass
    def __init__(self, id, nome, cpf, email, telefone):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    def criarUsuario(self, id, nome, cpf, email, telefone):
        u = Usuario(id, nome, cpf, email, telefone)
        self.lista.append(u)
        return u

    def listarUsuario(self):
        for x in self.lista:
            print(x.id)
            print(x.nome)
            print(x.cpf)
            print(x.email)
            print(x.telefone)
        #print('id:', self._id)
        #print('nome:', self._nome)
        #print('cpf:', self._cpf)
        #print('email:', self._email)
        #print('telefone:', self._telefone)

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
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
from entidades.usuario import Usuario

class UsuarioDao:

    def criar(id, nome, cpf, email, telefone):
        u = Usuario(id, nome, cpf, email, telefone)
        return u

    def listar(self):
        print('id:', self._id)
        print('nome:', self._nome)
        print('cpf:', self._cpf)
        print('email:', self._email)
        print('telefone:', self._telefone)

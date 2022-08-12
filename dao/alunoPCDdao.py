from entidades.alunoPCD import AlunoPCD

class AlunoDao:

    def __init__(self):
        self._alunosPCD = []

    def criaAlunoPCD(self, alunoPcd):
        self._alunosPCD.append(alunoPcd)

    def removeAlunoPCD(self, alunoPcd):
        self._alunosPCD.remove(alunoPcd)

    def listar(self):
        for aluno in self._alunosPCD:
            print(f'Nome: {aluno.nome}')
            print(f'Matricula: {aluno.matricula}')
            print(f'Cpf: {aluno.cpf}')

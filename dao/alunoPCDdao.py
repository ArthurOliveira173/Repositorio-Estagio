from entidades.alunoPcd import AlunoPcd
from conexao.conexaoBD import ConexaoBD

import mysql.connector

class AlunoDao:

    def __init__(self):
        self._alunosPcd = []

    def AdicionarAlunoPcd(self, alunoPcd):
        self._alunosPcd.append(alunoPcd)

    def removeAlunoPcd(self, alunoPcd):
        self._alunosPcd.remove(alunoPcd)

    def listar(self):
        for aluno in self._alunosPcd:
            print(f'Nome: {aluno.nome}')
            print(f'Matricula: {aluno.matricula}')
            print(f'Cpf: {aluno.cpf}')

from entidades.alunoPcd import AlunoPcd
from conexao.conexaoBD import ConexaoBD

import mysql.connector

class AlunoDao:
    _conexao = ConexaoBD.criarConexao("root", "tesi1")
    def __init__(self):
        pass

    @property
    def conexao(self):
        return self._conexao

    @conexao.setter
    def conexao(self, conexao):
        self._conexao = conexao

    def AdicionarAlunoPcd(self):

        cursor = self._conexao.cursor()

        sql = "INSERT INTO aluno_pcd (alu_id, alu_nome, alu_cpf, alu_sexo, alu_email, alu_telefone, alu_matricula, alu_deficiencias, alu_Periodo_Academico, alu_data_nascimento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (4, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
        cursor.execute(sql, val)

        self._conexao.commit()

    def removeAlunoPcd(self, alunoPcd):
        self._alunosPcd.remove(alunoPcd)

    def listar(self):
        for aluno in self._alunosPcd:
            print(f'Nome: {aluno.nome}')
            print(f'Matricula: {aluno.matricula}')
            print(f'Cpf: {aluno.cpf}')

from entidades.alunoPcd import AlunoPcd
from conexao.conexaoBD import ConexaoBD

import mysql.connector

class AlunoDao:
    _conexao = ConexaoBD.criarConexao("root", "tesi1")
    def __init__(self):
        pass

    def AdicionarAlunoPcd(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO aluno_pcd (alu_id, alu_nome, alu_cpf, alu_email, alu_telefone, alu_matricula, alu_deficiencias, alu_Periodo_Academico, alu_data_nascimento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoAlunoPcd(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM aluno_pcd")
        resultSet = cursor.fetchall()

        for aluno in resultSet:
            print(aluno)

    def listarAlunoPcd(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM aluno_pcd WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        for aluno in resultSet:
            print(aluno)

    def removeAlunoPcd(self, alunoPcd):
        self._alunosPcd.remove(alunoPcd)

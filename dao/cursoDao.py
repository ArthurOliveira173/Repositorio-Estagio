from conexao.conexaoBD import ConexaoBD

import mysql.connector

class CursoDao:
    _conexao = ConexaoBD.criarConexao("root", "bruno")
    def __init__(self):
        pass

    def AdicionarCurso(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO cursos (cur_id, cur_nome, cur_quant_periodos) VALUES (%s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoCurso(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM cursos")
        resultSet = cursor.fetchall()

        return resultSet
        # for curso in resultSet:
        #     print(curso)

    def listarCurso(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM cursos WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for curso in resultSet:
        #     print(curso)

    def removeCurso(self, curso):
        self._curso.remove(curso)

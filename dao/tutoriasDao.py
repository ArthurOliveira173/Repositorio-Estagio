from conexao.conexaoBD import ConexaoBD

class TutoriasDao:
    _conexaoBD = ConexaoBD()
    _conexao = _conexaoBD.criarConexao()

    def __init__(self):
        pass

    def AdicionarTutoria(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO tutoria (AsTut_id, AsTut_inicio, AsTut_fim, AsTut_tutor, AsTut_acompanhamento) VALUES (%s, %s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoTutoria(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM tutoria")
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def listarTutoria(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM tutoria WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def alterarTutoria(self, atributo, valor, linha_id):
        cursor = self._conexao.cursor()
        sql = "UPDATE tutoria SET {0} = '{1}' WHERE AsTut_id = {2}".format(atributo, valor, linha_id)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) afetadas")

    def removerTutoria(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "DELETE FROM tutoria WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) deletadas")
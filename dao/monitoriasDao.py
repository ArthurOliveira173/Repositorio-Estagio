from conexao.conexaoBD import ConexaoBD

class MonitoriasDao:
    _conexaoBD = ConexaoBD()
    _conexao = _conexaoBD.criarConexao()

    def __init__(self):
        pass

    def AdicionarMonitoria(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO monitoria (AsMon_id, AsMon_inicio, AsMon_fim, AsMon_monitor, AsMon_acompanhamento) VALUES (%s, %s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoMonitoria(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM monitoria")
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def listarMonitoria(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM monitoria WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def alterarMonitoria(self, atributo, valor, linha_id):
        cursor = self._conexao.cursor()
        sql = "UPDATE monitoria SET {0} = '{1}' WHERE AsMon_id = {2}".format(atributo, valor, linha_id)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) afetadas")

    def removerTutoria(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "DELETE FROM monitoria WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) deletadas")
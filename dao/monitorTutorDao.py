from conexao.conexaoBD import ConexaoBD

class MonitorTutorDao:
    _conexaoBD = ConexaoBD()
    _conexao = _conexaoBD.criarConexao()

    def __init__(self):
        pass

    def AdicionarMonitorTutor(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO interprete (int_id, int_nome, int_cpf, int_sexo, int_email, int_telefone) VALUES (%s, %s, %s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoMonitorTutor(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM interprete")
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def listarMonitorTutor(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM interprete WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for interprete in resultSet:
        #     print(interprete)

    def alterarMonitorTutor(self, atributo, valor, linha_id):
        cursor = self._conexao.cursor()
        sql = "UPDATE interprete SET {0} = '{1}' WHERE int_id = {2}".format(atributo, valor, linha_id)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) afetadas")

    def removerMonitorTutor(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "DELETE FROM interprete WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) deletadas")
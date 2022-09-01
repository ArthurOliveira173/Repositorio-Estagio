from conexao.conexaoBD import ConexaoBD

class AvisosDao:
    _conexaoBD = ConexaoBD()
    _conexao = _conexaoBD.criarConexao()

    def __int__(self):
        pass

    def adicionarAviso(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO avisos (avi_id, avi_titulo, avi_descricao, avi_data) " \
              "VALUES (%s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoAvisos(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM avisos")
        resultSet = cursor.fetchall()

        return resultSet

    def listarAvisos(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM avisos WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet

    def alterarAviso(self, atributo, valor, linha_id):
        cursor = self._conexao.cursor()
        sql = "UPDATE avisos SET {0} = '{1}' WHERE avi_id = {2}".format(atributo, valor, linha_id)
        cursor.execute(sql)
        self._conexao.commit()

        print(cursor.rowcount, "linha(s) afetadas")

    def removerAviso(self, atributo, valor):
        cursor = AvisosDao._conexao.cursor()
        sql = "DELETE FROM avisos WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        AvisosDao._conexao.commit()
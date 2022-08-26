from conexao.conexaoBD import ConexaoBD

class AvisosDao:
    _conexao = ConexaoBD.criarConexao('root', 'root123$')

    def __int__(self):
        pass

    def adicionarAviso(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO avisos (avi_id, avi_titulo, avi_descricao, avi_data, avi_arquivos) " \
              "VALUES (%s, %s, %s, %s, %s)"
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

    def removerAviso(atributo, valor):
        cursor = AvisosDao._conexao.cursor()
        sql = "DELETE FROM avisos WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        AvisosDao._conexao.commit()
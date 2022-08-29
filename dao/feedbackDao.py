from conexao.conexaoBD import ConexaoBD

class FeedbackDao:
    _conexao = ConexaoBD.criarConexao("root", "tesi1")
    def __init__(self):
        pass

    def AdicionarFeedback(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO feedback (fee_id, fee_titulo, fee_descricao, fee_data) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoFeedback(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM feedback")
        resultSet = cursor.fetchall()

        return resultSet
        # for disciplina in resultSet:
        #     print(disciplina)

    def listarFeedback(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM feedback WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for disciplina in resultSet:
        #     print(disciplina)

    def removerFeedback(atributo, valor):
        cursor = FeedbackDao._conexao.cursor()
        sql = "DELETE FROM feedback WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)

        FeedbackDao._conexao.commit()

        print(cursor.rowcount, "linha(s) deletadas")
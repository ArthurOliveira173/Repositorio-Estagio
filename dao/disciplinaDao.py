from conexao.conexaoBD import ConexaoBD

class DisciplinaDao:
    _conexaoBD = ConexaoBD()
    _conexao = _conexaoBD.criarConexao()

    def __init__(self):
        pass

    def AdicionarDisciplina(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO disciplinas (dis_id, dis_nome) VALUES (%s, %s)"
        val = vetorAtributos
        cursor.execute(sql, val)

        self._conexao.commit()

    def listarTudoDisciplina(self):
        cursor = self._conexao.cursor()
        cursor.execute("SELECT * FROM disciplinas")
        resultSet = cursor.fetchall()

        return resultSet
        # for disciplina in resultSet:
        #     print(disciplina)

    def listarDisciplina(self, atributo, valor):
        cursor = self._conexao.cursor()
        sql = "SELECT * FROM disciplinas WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)
        resultSet = cursor.fetchall()

        return resultSet
        # for disciplina in resultSet:
        #     print(disciplina)

    def removerDisciplina(self, atributo, valor):
        cursor = DisciplinaDao._conexao.cursor()
        sql = "DELETE FROM disciplinas WHERE {0} = '{1}'".format(atributo, valor)
        cursor.execute(sql)

        DisciplinaDao._conexao.commit()

        print(cursor.rowcount, "linha(s) deletadas")
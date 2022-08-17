import mysql.connector

class ConexaoBD:
    def criarConexao(usuario, senha):
        try:
            #Conecta ao servidor e banco MySQL
            cnx = mysql.connector.connect(
              host="127.0.0.1",
              port=3306,
              user=usuario,
              password=senha,
              database="estagio"
            )
            return cnx
        except:
            print("Erro ao tentar conectar ao banco MySQL")

# cnx = ConexaoBD.criarConexao("root", "tesi1")
# print(cnx)
# #Captura o cursor
# cur = cnx.cursor()
# #Executa a consulta
# cur.execute("select * from disciplinas;")
# #Coleta 1 resultado
# row = cur.fetchone()
# print("""disciplina 1:
#     id: {0}
#     descricao: {1}""".format(row[0],row[1]))
# # Close connection
# cnx.close()
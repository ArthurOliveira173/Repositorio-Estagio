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
              database="concursos"
            )
            return cnx
        except:
            print("Erro ao tentar conectar ao banco MySQL")

# cnx = ConexaoBD.criarConexao("root", "")
# print(cnx)
# #Captura o cursor
# cur = cnx.cursor()
# #Executa a consulta
# cur.execute("select * from boletos;")
# #Coleta 1 resultado
# row = cur.fetchone()
# print("""boleto 1:
#     id: {0}
#     cod_barras: {1}
#     data_vencimento: {2}
#     valor: {3}""".format(row[0],row[1],row[2],row[3]),)
# # Close connection
# cnx.close()
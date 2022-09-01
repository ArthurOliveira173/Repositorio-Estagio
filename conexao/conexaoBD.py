import mysql.connector

class ConexaoBD:
    def __init__(self):
        pass

    def criarConexao(self):
        try:
            #Conecta ao servidor e banco MySQL
            cnx = mysql.connector.connect(
              host="127.0.0.1",
              port=3306,
              user="root",
              password="tesi1",
              database="estagio"
            )
            return cnx
        except:
            print("Erro ao tentar conectar ao banco MySQL")

# # Imprimindo conexao
# cnx = ConexaoBD.criarConexao()
# print(cnx)

# # Fechando conexao
# cnx.close()
from conexao.conexaoBD import ConexaoBD

class MonitorTutorDao:
    _conexao = ConexaoBD.criarConexao('root', 'root123$')

    def __int__(self):
        pass


    def adicionarMonitorTutor(self, vetorAtributos):
        cursor = self._conexao.cursor()
        sql = "INSERT INTO monitor_tutor (mon_id, mon_nome, mon_cpf, mon_sexo, mon_email, " \
              "mon_telefone, mon_matricula, mon_periodo_academico, mon_tipo, mon_arquivos) VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
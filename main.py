from dao.alunoDao import AlunoDao
from dao.avisosDao import AvisosDao
from entidades.alunoPcd import AlunoPcd
from entidades.avisos import Avisos

# alunoDao = AlunoDao()
# aluno1 = (8, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
# alunoDao.AdicionarAlunoPcd(aluno1)

# lista = alunoDao.listarTudoAlunoPcd()
# lista = alunoDao.listarAlunoPcd("alu_id", 3)
# for aluno in lista:
#     print(aluno)

#lista = AlunoPcd.getAlunosLista(AlunoPcd)
#for aluno in lista:
#    print(aluno.nome)

#excluindo = AlunoDao.removeAlunoPcd('alu_id', 12)
avisosdao = AvisosDao()
'''
aviso1 = Avisos.CriarAviso(1, "Dia das Crianças", "12 de outubro", "2022-10-12", "avi_arquivos")
aviso2 = Avisos.CriarAviso(2, "Eventos para VOCE", "Festa da amizade", "2022-10-15", "avi_arquivos")
aviso3 = Avisos.CriarAviso(3, "Titulo 3", "descricao 3", "2022-10-16", "avi_arquivos")
aviso4 = Avisos.CriarAviso(4, "Titulo 4", "descricao 4", "2022-10-17", "avi_arquivos")
aviso5 = Avisos.CriarAviso(5, "Titulo 5", "descricao 5", "2022-10-18", "avi_arquivos")
'''

#avisosdao.adicionaAviso(aviso2)
#avisosdao.adicionaAviso(aviso3)
#avisosdao.adicionaAviso(aviso4)
#avisosdao.adicionaAviso(aviso5)

lista = avisosdao.listarTudoAvisos()
for aviso in lista:
    print(aviso)
print()
lista2 = avisosdao.listarAvisos('avi_id', 1)
for aviso in lista2:
    print(aviso)

avisosdao.removerAviso("avi_id", 1)

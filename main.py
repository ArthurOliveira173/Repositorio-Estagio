from entidades.alunoPcd import AlunoPcd
from entidades.curso import Curso
from entidades.disciplina import Disciplina
from entidades.feedback import Feedback
from entidades.avisos import Avisos
from dao.alunoDao import AlunoDao
from dao.cursoDao import CursoDao
from dao.disciplinaDao import DisciplinaDao
from dao.feedbackDao import FeedbackDao
from dao.avisosDao import AvisosDao

#======================================================================================================================#
# ALUNO
#======================================================================================================================#
avisoDao = AvisosDao()

aviso1 = Avisos.CriarAviso(1, "Titulo 1", "Descricao 1", "2020-08-01")
aviso2 = Avisos.CriarAviso(2, "Titulo 2", "Descricao 2", "2021-08-20")
aviso3 = Avisos.CriarAviso(3, "Titulo 3", "Descricao 3", "2021-11-23")
aviso4 = Avisos.CriarAviso(4, "Titulo 4", "Descricao 4", "2022-03-04")

avisoDao.alterarAviso('avi_titulo', "Titulo 3 alterado", 3)
avisoDao.alterarAviso("avi_descricao", "Descricao 2 alterada", 2)

avisoDao.removerAviso("avi_id", 4)

lista = avisoDao.listarTudoAvisos()
lista2 = avisoDao.listarAvisos("avi_id", 3)
for aviso in lista:
    print(aviso)
print()
for aviso in lista2:
    print(aviso)

# #======================================================================================================================#
# # CURSO
# #======================================================================================================================#
# cursoDao = CursoDao()
#
# # curso1 = Curso.CriarCurso(1, "Nome curso", 8)
# # curso1 = Curso.CriarCurso(2, "Nome curso2", 8)
# # curso1 = Curso.CriarCurso(3, "Nome curso3", 8)
# # curso1 = Curso.CriarCurso(4, "Nome curso4", 8)
#
# CursoDao.removerCurso("cur_id", 4)
#
# lista = cursoDao.listarTudoCurso()
# lista2 = cursoDao.listarCurso("cur_id", 3)
# for curso in lista:
#     print(curso)
# print()
# for curso in lista2:
#     print(curso)

#======================================================================================================================#
# ALUNO
#======================================================================================================================#
alunoDao = AlunoDao()
###### aluno1 = (8, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
###### alunoDao.AdicionarAlunoPcd(aluno1)
#
# aluno = AlunoPcd.CriarAlunoPcd(1, "carlos", "33344411100", "M", "email", "telefone", "20220400006",
#                                "deficiencia", "periodo", "2000-08-08")
# aluno2 = AlunoPcd.CriarAlunoPcd(2, "manoel", "33344411100", "M", "email", "telefone", "20220400006",
#                                  "deficiencia", "periodo", "2020-12-09")
# aluno3 = AlunoPcd.CriarAlunoPcd(3, "Maria", "33344411100", "F", "email", "telefone", "20220400006",
#                                "deficiencia", "periodo", "2000-08-08")
# aluno4 = AlunoPcd.CriarAlunoPcd(4, "Beatriz", "33344411100", "F", "email", "telefone", "20220400006",
#                                  "deficiencia", "periodo", "2020-12-09")
#
# alunoDao.alterarAlunoPcd('alu_nome', "Ana", 3)
# alunoDao.alterarAlunoPcd("alu_data_nascimento", "1999-05-20", 2)
#
# alunoDao.removerAlunoPcd("alu_id", 4)
#
# lista = alunoDao.listarTudoAlunoPcd()
# lista2 = alunoDao.listarAlunoPcd("alu_id", 3)
# for aluno in lista:
#     print(aluno)
# print()
# for aluno in lista2:
#     print(aluno)
#
# #======================================================================================================================#
# # DISCIPLINA
# #======================================================================================================================#
# disciplinaDao = DisciplinaDao()
#
# disciplina1 = Disciplina.CriarDisciplina(1, "Nome disciplina")
# disciplina2 = Disciplina.CriarDisciplina(2, "Nome disciplina2")
# disciplina3 = Disciplina.CriarDisciplina(3, "Nome disciplina3")
# disciplina4 = Disciplina.CriarDisciplina(4, "Nome disciplina4")
#
# DisciplinaDao.removerDisciplina("dis_id", 4)
#
# lista = disciplinaDao.listarTudoDisciplina()
# lista2 = disciplinaDao.listarDisciplina("dis_id", 3)
# for disciplina in lista:
#     print(disciplina)
# print()
# for disciplina in lista2:
#     print

#======================================================================================================================#
# FEEDBACK
#======================================================================================================================#
# feedbackDao = FeedbackDao()
#
# feedback1 = Feedback.CriarFeedback(1, "Título 1", "descricao 1", "2000-08-20")
# feedback2 = Feedback.CriarFeedback(2, "Título 2", "descricao 2", "2000-12-01")
# feedback3 = Feedback.CriarFeedback(3, "Título 3", "descricao 3", "2001-09-08")
# feedback4 = Feedback.CriarFeedback(4, "Título 4", "descricao 4", "2001-09-02")
#
# FeedbackDao.removerFeedback("fee_id", 4)
#
# lista = feedbackDao.listarTudoFeedback()
# lista2 = feedbackDao.listarFeedback("fee_id", 3)
# for feedback in lista:
#     print(feedback)
# print()
# for feedback in lista2:
#     print(feedback)

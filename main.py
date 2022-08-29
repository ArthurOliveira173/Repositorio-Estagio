from entidades.alunoPcd import AlunoPcd
from entidades.curso import Curso
from entidades.disciplina import Disciplina
from entidades.feedback import Feedback
from dao.alunoDao import AlunoDao
from dao.cursoDao import CursoDao
from dao.disciplinaDao import DisciplinaDao
from dao.feedbackDao import FeedbackDao

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
#alunoDao = AlunoDao()
###### aluno1 = (8, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
###### alunoDao.AdicionarAlunoPcd(aluno1)

# aluno = AlunoPcd.CriarAlunoPcd(3, "carlos", "33344411100", "M", "email", "telefone", "20220400006",
#                                "deficiencia", "periodo", "2000-08-08")
# aluno2 = AlunoPcd.CriarAlunoPcd(4, "manoel", "33344411100", "M", "email", "telefone", "20220400006",
#                                 "deficiencia", "periodo", "2020-12-09")
#
# AlunoDao.removerAlunoPcd("alu_id", 4)
#
# lista = alunoDao.listarTudoAlunoPcd()
# lista2 = alunoDao.listarAlunoPcd("alu_id", 3)
# for aluno in lista:
#     print(aluno)
# print()
# for aluno in lista2:
#     print(aluno)

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

from entidades.alunoPcd import AlunoPcd
from entidades.avisos import Avisos
from entidades.curso import Curso
from entidades.disciplina import Disciplina
from entidades.feedback import Feedback
from entidades.interprete import Interprete
from dao.alunoDao import AlunoDao
from dao.avisosDao import AvisosDao
from dao.cursoDao import CursoDao
from dao.disciplinaDao import DisciplinaDao
from dao.feedbackDao import FeedbackDao
from dao.interpreteDao import InterpreteDao

#======================================================================================================================#
# ALUNO
#======================================================================================================================#
# alunoDao = AlunoDao()
#
# alunoDao.AdicionarAlunoPcd((1, "carlos", "33344411100", "M", "email", "telefone", "20220400006",
#                                 "deficiencia", "periodo", "2000-08-08"))
# alunoDao.AdicionarAlunoPcd((2, "manoel", "33344411100", "M", "email", "telefone", "20220400006",
#                                  "deficiencia", "periodo", "2020-12-09"))
# alunoDao.AdicionarAlunoPcd((3, "Maria", "33344411100", "F", "email", "telefone", "20220400006",
#                                "deficiencia", "periodo", "2000-08-08"))
# alunoDao.AdicionarAlunoPcd((4, "Beatriz", "33344411100", "F", "email", "telefone", "20220400006",
#                                  "deficiencia", "periodo", "2020-12-09"))
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
#======================================================================================================================#
# AVISO
#======================================================================================================================#
# avisoDao = AvisosDao()
#
# avisoDao.adicionarAviso((1, "Titulo 1", "Descricao 1", "2020-08-01"))
# avisoDao.adicionarAviso((2, "Titulo 2", "Descricao 2", "2021-08-20"))
# avisoDao.adicionarAviso((3, "Titulo 3", "Descricao 3", "2021-11-23"))
# avisoDao.adicionarAviso((4, "Titulo 4", "Descricao 4", "2022-03-04"))
#
# avisoDao.alterarAviso('avi_titulo', "Titulo 3 alterado", 3)
# avisoDao.alterarAviso("avi_descricao", "Descricao 2 alterada", 2)
#
# avisoDao.removerAviso("avi_id", 4)
#
# lista = avisoDao.listarTudoAvisos()
# lista2 = avisoDao.listarAvisos("avi_id", 3)
# for aviso in lista:
#     print(aviso)
# print()
# for aviso in lista2:
#     print(aviso)
#
# #======================================================================================================================#
# # CURSO
# #======================================================================================================================#
# cursoDao = CursoDao()
#
# cursoDao.AdicionarCurso((1, "Nome curso", 8))
# cursoDao.AdicionarCurso((2, "Nome curso2", 8))
# cursoDao.AdicionarCurso((3, "Nome curso3", 8))
# cursoDao.AdicionarCurso((4, "Nome curso4", 8))
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
#
# #======================================================================================================================#
# # DISCIPLINA
# #======================================================================================================================#
# disciplinaDao = DisciplinaDao()
#
# disciplinaDao.AdicionarDisciplina((1, "Nome disciplina"))
# disciplinaDao.AdicionarDisciplina((2, "Nome disciplina2"))
# disciplinaDao.AdicionarDisciplina((3, "Nome disciplina3"))
# disciplinaDao.AdicionarDisciplina((4, "Nome disciplina4"))
#
# DisciplinaDao.removerDisciplina("dis_id", 4)
#
# lista = disciplinaDao.listarTudoDisciplina()
# lista2 = disciplinaDao.listarDisciplina("dis_id", 3)
# for disciplina in lista:
#     print(disciplina)
# print()
# for disciplina in lista2:
#     print(disciplina)
#
#======================================================================================================================#
# FEEDBACK
#======================================================================================================================#
# feedbackDao = FeedbackDao()
#
# feedbackDao.AdicionarFeedback((1, "Título 1", "descricao 1", "2000-08-20"))
# feedbackDao.AdicionarFeedback((2, "Título 2", "descricao 2", "2000-12-01"))
# feedbackDao.AdicionarFeedback((3, "Título 3", "descricao 3", "2001-09-08"))
# feedbackDao.AdicionarFeedback((4, "Título 4", "descricao 4", "2001-09-02"))
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
#
#======================================================================================================================#
# INTERPRETE
#======================================================================================================================#
interpreteDao = InterpreteDao()

interpreteDao.AdicionarInterprete((1, "Guilherme", "33344411100", "M", "email", "telefone"))
interpreteDao.AdicionarInterprete((2, "Luiza", "33344411100", "F", "email", "telefone"))
interpreteDao.AdicionarInterprete((3, "Bruno", "33344411100", "F", "email", "telefone"))
interpreteDao.AdicionarInterprete((4, "Helena", "33344411100", "F", "email", "telefone"))

interpreteDao.alterarInterprete('int_nome', "Tania", 3)
interpreteDao.alterarInterprete("int_telefone", "68995572829", 2)

interpreteDao.removerInterprete("int_id", 4)

lista = interpreteDao.listarTudoInterprete()
lista2 = interpreteDao.listarInterprete("int_id", 3)
for interprete in lista:
    print(interprete)
print()
for interprete in lista2:
    print(interprete)
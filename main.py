from entidades.alunoPcd import AlunoPcd
from entidades.Curso import Cursos
from dao.alunoDao import AlunoDao
from dao.cursoDao import CursoDao

# alunoDao = AlunoDao()
# aluno1 = (8, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
# alunoDao.AdicionarAlunoPcd(aluno1)

# lista = alunoDao.listarTudoAlunoPcd()
# lista = alunoDao.listarAlunoPcd("alu_id", 3)
# for aluno in lista:
#     print(aluno)

cursoDao = CursoDao()

# curso2 = Cursos.CriarCurso(2, "sistema de inforamção", 8)
# curso3 = Cursos.CriarCurso(3, "Letras Libras", 8)

lista = cursoDao.listarTudoCurso()
lista2 = cursoDao.listarCurso("cur_id", 3)
for curso in lista:
     print(curso)
print()
for curso in lista2:
     print(curso)

# aluno = AlunoPcd.CriarAlunoPcd(11, "carlos", "33344411100", "M", "email", "telefone", "20220400006",
#                                "deficiencia", "periodo", "2000-08-08")
# aluno2 = AlunoPcd.CriarAlunoPcd(12, "manoel", "33344411100", "M", "email", "telefone", "20220400006",
#                                 "deficiencia", "periodo", "2020-12-09")
from entidades.alunoPcd import AlunoPcd
from dao.alunoDao import AlunoDao

# alunoDao = AlunoDao()
# aluno1 = (8, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
# alunoDao.AdicionarAlunoPcd(aluno1)

# lista = alunoDao.listarTudoAlunoPcd()
# lista = alunoDao.listarAlunoPcd("alu_id", 3)
# for aluno in lista:
#     print(aluno)


aluno = AlunoPcd.CriarAlunoPcd(11, "carlos", "33344411100", "M", "email", "telefone", "20220400006",
                               "deficiencia", "periodo", "2000-08-08")
aluno2 = AlunoPcd.CriarAlunoPcd(12, "manoel", "33344411100", "M", "email", "telefone", "20220400006",
                                "deficiencia", "periodo", "2020-12-09")
lista = AlunoPcd.getAlunosLista(AlunoPcd)
for aluno in lista:
    print(aluno.nome)
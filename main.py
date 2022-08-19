from entidades.alunoPcd import AlunoPcd
from dao.alunoPCDdao import AlunoDao

alunoDao = AlunoDao()

#aluno1 = (6, "John", "asd", "M", "asd", "asd", "asd", "asd", "asd", "2000-08-08")
#alunoDao.AdicionarAlunoPcd(aluno1)
#alunoDao.listarTudoAlunoPcd()
#alunoDao.listarAlunoPcd("alu_id", 3)

aluno = AlunoPcd.CriarAlunoPcd(1, "carlos", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                  "disciplinas", "periodo", "deficiencia", "data_nascimento")

aluno2 = AlunoPcd.CriarAlunoPcd(2, "manoel", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                  "disciplinas", "periodo", "deficiencia", "data_nascimento")

lista = AlunoPcd.getAlunosLista(AlunoPcd)
for aluno in lista:
    print(aluno.nome)
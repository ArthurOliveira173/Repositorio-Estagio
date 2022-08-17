from entidades.alunoPcd import AlunoPcd
from entidades.interprete import Interprete
from dao.alunoPCDdao import AlunoDao
from entidades.avisos import Avisos

alunosDao = AlunoDao()

aluno = AlunoPcd(1, "carlos", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")

aluno2 = AlunoPcd(2, "manoel", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")

avisos = Avisos(2, "casa", "porta janela", "28-05-2021", 1)

print("id do aviso:", avisos.id)

alunosDao.AdicionarAlunoPcd(aluno)
alunosDao.AdicionarAlunoPcd(aluno2)
alunosDao.removeAlunoPcd(aluno)

alunosDao.listar()
interprete = Interprete(2, "n1", "cpf", "email", "telefone")


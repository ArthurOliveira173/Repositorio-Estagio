from entidades.alunoPCD import AlunoPCD
from entidades.interprete import Interprete
from dao.alunoPCDdao import AlunoDao
from entidades.avisos import Avisos

alunosDao = AlunoDao()

aluno = AlunoPCD(1, "carlos", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")

aluno2 = AlunoPCD(2, "manoel", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")

avisos = Avisos(2, "casa", "porta janela", "28-05-2021", 1)

print("id do aviso:", avisos.id)

alunosDao.criaAlunoPCD(aluno)
alunosDao.criaAlunoPCD(aluno2)
alunosDao.removeAlunoPCD(aluno)

alunosDao.listar()
interprete = Interprete(2, "n1", "cpf", "email", "telefone")


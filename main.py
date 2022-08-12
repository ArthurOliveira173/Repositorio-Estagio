from entidades.alunoPCD import AlunoPCD
from entidades.interprete import Interprete
from dao.alunoPCDdao import AlunoDao
from entidades.avisos import Avisos

alunosDao = AlunoDao()

aluno = AlunoPCD(1, "carlos", "333.444.111-00", "email", "telefone", "20220400006", "S.I",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")
#template aviso(id, titulo, descricao,data, tipo)
avisos = Avisos(2, "casa", "porta janela", "28-05-2021", 1)
#system.out.println -> Java
#print() -> python
print("id do aviso:", avisos.id)
alunosDao.criaAlunoPCD(aluno)
alunosDao.listar()
interprete = Interprete(2, "n1", "cpf", "email", "telefone")


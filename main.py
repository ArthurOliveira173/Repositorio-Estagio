from entidades.alunoPCD import AlunoPCD
from entidades.interprete import Interprete
aluno = AlunoPCD(1, "nome", "cpf", "email", "telefone", "matricula", "curso",
                 "disciplinas", "periodo", "deficiencia", "data_nascimento")

print(f'{aluno} wrwerv wer {aluno.id}')

interprete = Interprete(2, "n1", "cpf", "email", "telefone")

print(interprete.nome)
interprete.alteraNome("Correto....")
print(interprete.nome)


from usuario import Usuario
from enums.moniTutoEnum import MoniTutoEnum

class Tu(Usuario):
   _monitorTutor = []

   def __init__(self, id, nome, cpf, sexo, email, telefone, matricula,
                curso, periodo_academico, tipo, arquivo, aluno):
      self._id = id
      self._nome = nome
      self._cpf = cpf
      self._sexo = sexo
      self._email = email
      self._telefone = telefone
      self._matricula = matricula
      self._curso = curso
      self._periodo = periodo_academico
      self._tipo = tipo
      self._arquivo = arquivo
      self._aluno = aluno

   def getListaMonitorTutor(self):
      lista = self._monitorTutor[:]
      return lista

   @property
   def id(self):
      return self._id

   @id.setter
   def id(self, id):
      self._id = id

   @property
   def nome(self):
      return self._nome

   @nome.setter
   def nome(self, nome):
      self._nome = nome

   @property
   def cpf(self):
      return self._cpf

   @cpf.setter
   def cpf(self, cpf):
      self._cpf = cpf

   @property
   def sexo(self):
      return self._sexo

   @sexo.setter
   def sexo(self, sexo):
      self._sexo = sexo

   @property
   def email(self):
      return self._email

   @email.setter
   def email(self, email):
      self._email = email

   @property
   def telefone(self):
      return self._telefone

   @telefone.setter
   def telefone(self, telefone):
      self._telefone = telefone

   @property
   def matricula(self):
      return self._matricula

   @matricula.setter
   def matricula(self, matricula):
      self._matricula = matricula

   @property
   def curso(self):
      return self._curso

   @curso.setter
   def curso(self, curso):
      self._curso = curso

   @property
   def periodo(self):
      return self._periodo

   @periodo.setter
   def periodo(self, periodo):
      self._periodo = periodo

   @property
   def tipo(self):
      return self._tipo

   @tipo.setter
   def tipo(self, tipo):
      self._tipo = tipo

   @property
   def arquivo(self):
      return self._arquivo

   @arquivo.setter
   def arquivo(self, arquivo):
      self._arquivo = arquivo

   @property
   def aluno(self):
      return self._aluno

   @aluno.setter
   def aluno(self, aluno):
      self._aluno = aluno
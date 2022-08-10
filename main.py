from entidades.usuario import Usuario
from dao.usuarioDao import UsuarioDao

u = Usuario.criar(Usuario , 1, "guilherme", "97927391726", "gui@gmail.com", "992876767")
u.listar()


import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture(scope='module')
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gera_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Henrique')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Henrique'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

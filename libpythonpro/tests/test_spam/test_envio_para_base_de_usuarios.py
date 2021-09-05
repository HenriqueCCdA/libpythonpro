from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('renzo@python.pro.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantáticos')


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ]
    ]
)
def test_qte_de_spam_enviados(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('renzo@python.pro.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantáticos')

    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('luciano@python.pro.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantáticos'
                                   )
    enviador.enviar.assert_called_once_with('luciano@python.pro.br',
                                            'renzo@python.pro.br',
                                            'Curso Python Pro',
                                            'Confira os módulos fantáticos')

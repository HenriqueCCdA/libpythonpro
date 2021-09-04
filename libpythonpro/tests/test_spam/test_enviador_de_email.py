import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_cria_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente',
                         ['henrique.ccda@gmail.com', 'foo@bar.com.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(remetente,
                                'henrique@poli.ufrj.br',
                                'Cursos Python Pro',
                                'Primeira turma Guido Von Rossum aberta.')

    assert remetente in resultado


@pytest.mark.parametrize('remetente',
                         ['', 'foo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        _ = enviador.enviar(remetente,
                            'henrique@poli.ufrj.br',
                            'Cursos Python Pro',
                            'Primeira turma Guido Von Rossum aberta.')

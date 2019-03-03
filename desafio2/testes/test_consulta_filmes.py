import unittest
from nose.tools import assert_equal
from consulta_filmes import ConsultaFilmes


class TestConsultaFilmes(unittest.TestCase):

    def setUp(self):
        self.consulta_filmes = ConsultaFilmes()

    def test_validar_titulo_ano_idioma(self):
        dados_filme = {
            'Title': 'The Social Network',
            'Year': '2010',
            'Language': 'English, French'
        }

        id_filme = "tt1285016"

        resultado = self.consulta_filmes.consulta_filmes_id(id_filme)[0]

        for k, v in dados_filme.items():
            assert_equal(dados_filme[k], resultado[k])

    def test_filmes_inexistente(self):
        id_filme = "filme inexistente"

        resultado = self.consulta_filmes.consulta_filmes_id(id_filme)[0]
        assert_equal(resultado['Error'], 'Incorrect IMDb ID.')


if __name__ == '__main__':
    unittest.main()
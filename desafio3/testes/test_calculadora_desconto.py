import unittest
from nose.tools import assert_equal
from carrinho_compras import CarrinhoCompras


class TestCalculadoraDesconto(unittest.TestCase):

    def setUp(self):
        self.carrinho = CarrinhoCompras()

    def test_desconto_10(self):
        produtos = [1, 5]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 130.50)

    def test_desconto_20(self):
        produtos = [2, 3, 4]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 159.60)

    def test_desconto_25(self):
        produtos = [2, 3, 4, 5]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 220.88)

    def test_desconto_30(self):
        produtos = [5, 5, 6, 6]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 420.0)

    def test_desconto_genero(self):
        produtos = [3]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 95.0)

    def test_sem_desconto_abaixo_10(self):
        produtos = [1]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 45.00)

    def test_sem_desconto_outro_genero(self):
        produtos = [5]
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 100.00)

    def test_passando_string_1(self):
        produtos = ['abacaxi']
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 0)

    def test_passando_string_2(self):
        produtos = [1, 2, 3, 'abacaxi']
        valor_compra = self.carrinho.calcula_valor_compra(produtos)
        assert_equal(valor_compra, 190.00)


if __name__ == '__main__':
    unittest.main()
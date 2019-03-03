from filmes import FILMES

class CarrinhoCompras(object):


    def calcula_valor_compra(self, ids):

        lista_filmes = []
        valor_compra = 0

        for id in ids:
            for k, v in FILMES.items():
                if v['id'] == id:
                    lista_filmes.append(v)
                    valor_compra += v['valor']
                    break

        if 100 < valor_compra < 200:
            valor_compra = valor_compra * 0.90

        elif 200 < valor_compra < 300:
            valor_compra = valor_compra * 0.80

        elif 300 < valor_compra < 400:
            valor_compra = valor_compra * 0.75

        elif valor_compra > 400:
            valor_compra = valor_compra * 0.70

        for filme in lista_filmes:
            if 'Ação' in filme['genero']:
                return round(valor_compra * 0.95, 2)

        return round(valor_compra, 2)

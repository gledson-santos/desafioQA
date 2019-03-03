
class Util(object):

    def limpa_nome_step(self, step):
        nome_step = str(step)
        lista_comando_step = ['given', 'then', 'when']

        for comando in lista_comando_step:
            if comando in nome_step:
                nome = nome_step.replace(comando, '').replace('<', '').replace('>', '').replace("'", '').replace(' ', '_').replace('"', '')

        return nome.lower()
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from features.utils.wait import Wait
from features.utils.web_app import webapp
from time import sleep

class GuiaMedicoPage():

    instance = None
    wait = Wait()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = GuiaMedicoPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.link_guia_medico = "//a[contains(.,'Guia Médico')]"
        self.input_pesquisa = "pesquisa"
        self.botao_pesquisar = "//button[@class='btn btn-primary no-margin btn-search-width']"
        self.campo_estado_e_cidade = "//div[@class='css-1hwfws3']"
        self.botao_pesquisar_avacado = "//button[@class='btn btn-success']"
        self.regioes_avancada = "//label[@class='margin-bottom fonte-padrao']"
        self.input_radio_regiao = 'div[1]/input'
        self.avancar_paginacao = 'proximo'
        self.listagem_medicos = '//div[@class="resultado-resumido padding relative"]'
        self.nome_medico = 'txt_nome_prestador'
        self.especialidade_medico = '//span[@id="txt_especialidade"]/../span[3]'
        self.servico_medico = '//span[@id="txt_grupos"]/../span[2]'
        self.endereco_medico = 'txt_endereco'

    def click_guia_medico(self):
        self.driver.find_element_by_xpath(self.link_guia_medico).click()

    def inclur_termo_pesquisa(self, termo):
        self.driver.find_element_by_name(self.input_pesquisa).send_keys(termo)

    def clicar_pesquisar(self):
        self.wait.aguardar_xpath_clicavel(self.botao_pesquisar)
        self.driver.find_element_by_xpath(self.botao_pesquisar).click()

    def selecionar_estado(self, estado):
        campos = self.driver.find_elements_by_xpath(self.campo_estado_e_cidade)
        _estado = campos[0]
        _estado.click()
        actions_estado = ActionChains(self.driver)
        actions_estado.send_keys(estado)
        actions_estado.key_down(Keys.ENTER)
        actions_estado.perform()

    def selecinar_cidade(self, cidade):
        campos = self.driver.find_elements_by_xpath(self.campo_estado_e_cidade)
        _cidade = campos[1]
        _cidade.click()
        actions_cidade = ActionChains(self.driver)
        actions_cidade.send_keys(cidade)
        actions_cidade.key_down(Keys.ENTER)
        actions_cidade.perform()

    def selecionar_regiao(self, regiao):
        self.wait.aguardar_elemento_ficar_visivel_xpath(self.regioes_avancada)
        sleep(2)
        regioes = self.driver.find_elements_by_xpath(self.regioes_avancada)
        for reg in regioes:
            if reg.text == regiao:
                id_radio = reg.find_element_by_xpath(self.input_radio_regiao)
                valor_input = id_radio.get_attribute('value')
                self.wait.aguardar_xpath_clicavel('//input[@value="' + valor_input + '"]')
                self.driver.find_element_by_xpath('//input[@value="' + valor_input + '"]').click()

    def click_pesquisa_avancada(self):
        self.driver.find_element_by_xpath(self.botao_pesquisar_avacado).click()

    def click_avancar_paginacao(self):
        try:
            self.driver.find_element_by_class_name(self.avancar_paginacao).click()
        except Exception as e:
            pass

    def coleta_detalhes_medicos(self, pagina):

        informacoes_medicos = []
        paginacao = 1

        while paginacao <= pagina:
            medicos = self.driver.find_elements_by_xpath(self.listagem_medicos)
            detalhes = {}
            for medico in medicos:
                detalhes['nome'] = medico.find_element_by_id(self.nome_medico).text
                try:
                    detalhes['especialidade'] = medico.find_element_by_xpath(self.especialidade_medico).text
                except:
                    detalhes['especialidade'] = 'NÃO HÁ'
                try:
                    detalhes['servicos'] = medico.find_element_by_xpath(self.servico_medico).text
                except:
                    detalhes['servicos'] = 'NÃO HÁ'

                detalhes['endereco'] = medico.find_element_by_id(self.endereco_medico).text

                informacoes_medicos.append(detalhes)
            paginacao += 1

            self.click_avancar_paginacao()

        return informacoes_medicos


guia_medico = GuiaMedicoPage()

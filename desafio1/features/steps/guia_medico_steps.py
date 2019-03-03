# encoding: iso-8859-1
from behave import *
from features.page.guia_medico_page import guia_medico
from nose.tools import assert_equals, assert_is_not

global filtro_pesquisa
filtro_pesquisa = {}


@step(u'que estou na tela guia médico')
def step_impl(context):
    guia_medico.click_guia_medico()


@step(u'que efetuo uma pesquisa por "{especialidade}"')
def step_impl(context, especialidade):
    filtro_pesquisa['especialidade'] = especialidade
    guia_medico.inclur_termo_pesquisa(especialidade)
    guia_medico.clicar_pesquisar()


@step(u'seleciono o estado "{estado}" cidade "{cidade}"')
def step_impl(context, estado, cidade):
    filtro_pesquisa['estado'] = estado
    filtro_pesquisa['cidade'] = cidade

    guia_medico.selecionar_estado(estado)
    guia_medico.selecinar_cidade(cidade)


@step(u'região "{regiao}"')
def step_impl(context, regiao):
    filtro_pesquisa['regiao'] = regiao

    guia_medico.selecionar_regiao(regiao)
    guia_medico.click_pesquisa_avancada()
    guia_medico.clicar_pesquisar()


@step(u'navego até a {pagina} pagina')
def step_impl(context, pagina=1):
    global dados_medicos
    dados_medicos = guia_medico.coleta_detalhes_medicos(int(pagina))

@step(u'não deve apresentar médicos da cidade "{cidade}"')
def step_impl(context, cidade):
    for medico in dados_medicos:
        cidade_medico = medico['endereco'].split('-')[1].split('/')[0].strip()
        assert_is_not(cidade_medico, cidade)

@step(u'vejo apenas médicos desta especialidade nesta região')
def step_impl(context):
    context.execute_steps('''
        Dado navego até a 1 pagina
    ''')
    for medico in dados_medicos:
        cidade_medico = medico['endereco'].split('-')[1].split('/')[0].strip()
        especialidade_medico = medico['especialidade'].split()[0].lower()

        if medico['especialidade'] != 'NÃO HÁ':
            assert_equals(especialidade_medico, filtro_pesquisa['especialidade'])
        else:
            assert_equals(medico['servicos'], filtro_pesquisa['filtro_pesquisa'])
        assert_equals(cidade_medico, filtro_pesquisa['cidade'])

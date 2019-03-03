# Created by gledsons at 25/02/2019
# encoding: iso-8859-1
# language: pt

Funcionalidade: Guia Medico
  # Enter feature description here


  Contexto:
    Dado que estou na tela guia médico


  Cenario: 1 - Validar o retorno da pesquisa por médicos e região
    Dado que efetuo uma pesquisa por "pediatria"
    Quando seleciono o estado "Rio de Janeiro" cidade "Rio de Janeiro"
    E região "UNIMED RIO"
    Então vejo apenas médicos desta especialidade nesta região


  Cenario: 2 - Validar o retorno da pesquisa por médicos e região até a pagina 3
    Dado que efetuo uma pesquisa por "médicos"
    Quando seleciono o estado "Rio de Janeiro" cidade "Rio de Janeiro"
    E região "UNIMED RIO"
    Então navego até a 3 pagina
    E não deve apresentar médicos da cidade "São Paulo"
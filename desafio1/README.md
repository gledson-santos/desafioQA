## Desafio 1
Projeto Automação de Teste baseia-se nas seguintes ferramentas:

* **Behave** - Para escrita dos testes em gherkin. [Behave Docs](http://pythonhosted.org/behave/)
* **Selenium Webdriver** - Para interação com o browser [Selenium Docs](http://selenium-python.readthedocs.io/getting-started.html)
* **Python: version 3.6** - Para a linguagem de programação [Site Python](https://www.python.org/)

## Instalação
`Obs.: Os passos a seguir são baseados no SO Windows.`

**Pré Requisitos**

- Python 3.6.1
- Máquina Virtualenv - [Veja Como instalar](https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/)
- Ter o repositório no local

## Passos para instalação

1. Instale o python no seu path. [Para mais detalhes](https://www.python.org/downloads/)
2. Abra o terminal
3. Instale uma máquina virtual com o seguinte comando **pip install virtualenv**
4. Criando o ambiente virtual:
    - No terminal, acesse a pasta de sua escolha e execute o comando **virtualenv virtualNoesis**
5. Inicie o ambiente virtual: **virtualNoesis\Scripts\activate**
6. Acesse a pasta desafio1, e instale as dependências com o seguinte comando: **pip install requirements.txt**
4. Incluir o chromedriver no ambiente path da máquina virtual criada
     - **Copiar o chromedriver contido na pasta drive**
     - **Colar o chromedriver na pasta Script dentro do virtualenv**
`virtualNoesis/Script`

## Execução dos testes

Dentro da pasta desafio1/feature, roda o seguinte comando
**behave  --junit**

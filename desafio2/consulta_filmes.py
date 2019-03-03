import requests
import json
from config import CHAVE_API


class ConsultaFilmes(object):

    def __init__(self):
        self.chave_api = CHAVE_API

    def consulta_filmes_id(self, id_filme):
        response = requests.get("http://www.omdbapi.com/?i={}&apikey={}".format(id_filme, self.chave_api))
        conteudo = json.loads(response.content.decode('utf-8'))
        http = response.status_code
        return conteudo, http

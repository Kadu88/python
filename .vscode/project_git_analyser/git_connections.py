import json
import os
import sys

from github import Github

from functions_git import buscar_repositorios_linguagem
from restkit import BasicAuth, Connection, Resource, request
from socketpool import ConnectionPool

pool = ConnectionPool(factory=Connection)
serverurl="https://api.github.com"
# or using an access token
token = os.environ.get('GIT_TOKEN')

def getRest(linguagem, pg_atual):
    qtd_por_pg = ('5')
    pg_inical = pg_atual
    url_chamada = ('https://api.github.com/search/repositories?page=%s&per_page=%s&q=topic:%s' % (pg_inical, qtd_por_pg, linguagem))
    resource = Resource(url_chamada, pool=pool )
    resource.charset = 'utf-8'
    headers = {'Content-Type' : 'application/json' }
    headers['Authorization'] = 'token %s' % token
    response = resource.get(headers = headers)
    #print('Next:')
    #print(response.next)
    repos = json.loads(response.body_string())
    return repos
import os
import sys
import json
from github import Github
from socketpool import ConnectionPool
from functions_git import buscar_repositorios_linguagem
from restkit import Resource, BasicAuth, Connection, request

pool = ConnectionPool(factory=Connection)
serverurl="https://api.github.com"

# or using an access token
token = os.environ.get('GIT_TOKEN')
g = Github(token)

resource = Resource('https://api.github.com/search/repositories?q=topic:JavaScript', pool=pool )
resource.charset = 'utf-8'
headers = {'Content-Type' : 'application/json' }
headers['Authorization'] = 'token %s' % token
#response = resource.get(params_dict='per_page=100')
response = resource.get(headers = headers)
repos = json.loads(response.body_string())

#print(type(repos))
#print(repos.keys())
#print(repos['total_count'])
#print(repos['items'])
#print(type(repos['items']))

lista_listas_linguagem = []

lista_linguagens = ['JavaScript', 'Python', 'Ruby', 'Java', 'PHP']
for linguagem in lista_linguagens:
    print(linguagem)
    lista_listas_linguagem = lista_listas_linguagem + buscar_repositorios_linguagem(linguagem, repos)

print('========================== Resultado Listado ==========================')

for lista_dados_item in lista_listas_linguagem:
    item = lista_dados_item['item']
    #print(item)
    linguagem_item = lista_dados_item['linguagem']
#    print(linguagem_item)
    contador = lista_dados_item['count']
#    print(contador)
    print('====')
    print(lista_dados_item['linguagem'], lista_dados_item['count'], item['name'], item['stargazers_count'])
#    print('Nome: %s  possui  estrelas' % item['name'], item['stargazers_count'])
#for item in lista_itens_geral:
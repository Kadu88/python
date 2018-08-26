import json
import os
import sys

from github import Github
from functions_git import buscar_repositorios_linguagem
from git_connections import getRest

counter_rep=0

def increment_count_repo():
    global counter_rep
    counter_rep = counter_rep+1

def zerar_count_repo():
    global counter_rep
    counter_rep = 0


lista_listas_linguagem = []

#lista_linguagens = ['JavaScript', 'Python', 'Ruby', 'Java', 'PHP']
lista_linguagens = ['Java']
pg_atual = 1

    
for linguagem in lista_linguagens:
    zerar_count_repo()
    for count in range(pg_atual, 4):
        repos = getRest(linguagem, pg_atual)
        increment_count_repo()
        lista_parametros = {'linguagem':linguagem, 'repos':repos, 'counter_rep':counter_rep}
        lista_listas_linguagem = lista_listas_linguagem + buscar_repositorios_linguagem(lista_parametros)
        pg_atual = pg_atual+1
    print(linguagem)    

print('========================== Resultado Listado ==========================')

for lista_dados_item in lista_listas_linguagem:
    item = lista_dados_item['item']
    linguagem_item = lista_dados_item['linguagem']
    contador = lista_dados_item['count']
    repositorio = lista_dados_item['repositorio']
#    print('====')
    print(linguagem_item, contador, item['name'], item['stargazers_count'])

#    print('**')
#    novo_repositorio = GitRepository(linguagem, item['url'], 0, item['git_commits_url'], item['git_commits_url'], item['git_commits_url'], item['git_commits_url'])
#(self, linguagem_repo, url_repository, commits_total_repo, commits_url, developers, core_developers, idade_repo):
#    print(repositorio.linguagem_repo)
#    url = (repositorio.url_repository)
#    print(url)
#    print(type(url))
#    print('**')

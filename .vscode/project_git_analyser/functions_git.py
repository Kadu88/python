#python functions
from git_respository import GitRepository
from program_4_know import increment_count_repo

def buscar_repositorios_linguagem(lista_parametros):
    linguagem = lista_parametros['linguagem']
    repos = lista_parametros['repos']
    counter_rep = lista_parametros['counter_rep']

    lista_itens_linguagem = []
    for item in repos['items']:
        increment_count_repo()
        counter_rep = counter_rep+1
        #print(count)
        #print(type(item['stargazers_count']))
        #print('Nome: %s  possui  estrelas' % item['name'], item['stargazers_count'])
        novo_repositorio = criar_repositorio(linguagem, counter_rep, item)
        lista_itens = {'linguagem':linguagem,'count':counter_rep, 'item':item, 'repositorio':novo_repositorio}
        lista_itens_linguagem.append(lista_itens)
    return lista_itens_linguagem


def criar_repositorio(linguagem, count, item):
    novo_repositorio = GitRepository(item['name'], linguagem, item['stargazers_count'], item['url'], 0, item['git_commits_url'], item['git_commits_url'], item['git_commits_url'], item['git_commits_url'])
    return novo_repositorio
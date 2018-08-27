#python functions
from git_respository import GitRepository
from program_4_know import increment_count_repo, get_count_repo

def buscar_repositorios_linguagem(linguagem, repos):

    lista_itens_linguagem = []
    for item in repos['items']:
        increment_count_repo()
        #print(count)
        #print(type(item['stargazers_count']))
        #print('Nome: %s  possui  estrelas' % item['name'], item['stargazers_count'])
        novo_repositorio = criar_repositorio(linguagem, get_count_repo, item)
        lista_itens = {'linguagem':linguagem,'count':get_count_repo, 'item':item, 'repositorio':novo_repositorio}
        lista_itens_linguagem.append(lista_itens)
    return lista_itens_linguagem


def criar_repositorio(linguagem, count, item):
    novo_repositorio = GitRepository(item['name'], linguagem, item['stargazers_count'], item['url'], 0, item['git_commits_url'], item['git_commits_url'], item['git_commits_url'], item['git_commits_url'])
    return novo_repositorio
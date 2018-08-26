#python functions
def buscar_repositorios_linguagem(linguagem, repos, counter_rep):
    lista_itens_linguagem = []
    for item in repos['items']:
        counter_rep = counter_rep+1
        #print(count)
        #print(type(item['stargazers_count']))
        #print('Nome: %s  possui  estrelas' % item['name'], item['stargazers_count'])
        lista_itens = {'linguagem':linguagem,'count':counter_rep, 'item':item}
        lista_itens_linguagem.append(lista_itens)
    return lista_itens_linguagem


#https://api.github.com/repos/yarnpkg/yarn/commits{/sha}'
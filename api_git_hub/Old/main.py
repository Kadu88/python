from github import Github

from github import Github

login=("")
senha=("")
g = Github(login, senha)

print(g.get_api_status())



#g = Github("")
#curl 'https://api.github.com/user/repos?page=2&per_page=100'

print('\n')

for repo in g.get_user().get_repos():
    print(repo.name)


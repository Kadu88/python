import json
from restkit import Resource, BasicAuth, Connection, request
from socketpool import ConnectionPool
import sys
from github import Github


pool = ConnectionPool(factory=Connection)
serverurl="https://api.github.com"

# or using an access token
g = Github(getToken())
token=(getToken)

# Github Enterprise with custom hostname
#g = Github(base_url="https://api.github.com/api/v3", token="")

# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print(repo.name)

#resource = Resource('https://api.github.com/user/repos', pool=pool)
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

count = 0

for item in repos['items']:
    count = count+1
    #print(count)
    #print(type(item['stargazers_count']))
    #print('Nome: %s  possui  estrelas' % item['name'], item['stargazers_count'])
    print(count, item['stargazers_count'])


#print(repos)
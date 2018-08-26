import json
import sys
from restkit import Resource, BasicAuth, Connection, request
from socketpool import ConnectionPool
from github import Github

pool = ConnectionPool(factory=Connection)
serverurl="https://api.github.com"

# Pass the username and password to the command line as arguements
#user = sys.argv[1]
#password = sys.argv[2]
#auth=BasicAuth(user, password)

user = ("")
password =("")
auth=BasicAuth(user, password)
token = ("")
print(token)
# Pass the username and password to the command line as arguements

"""
Once you have a token, you can pass that in the Authorization header
You can store this in a cache and throw away the user/password
This is just an example query.  See http://developer.github.com/v3/ 
for more about the url structure
"""
curl -H "Authorization: token " https://api.github.com
resource = Resource('https://api.github.com/kadu88', pool=pool)
headers = {'Content-Type' : 'application/json' }
#headers['Authorization'] = 'token %s' % token

response = resource.get(headers = headers)
repos = json.loads(response.body_string())
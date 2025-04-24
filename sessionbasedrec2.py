import requests


host = 'https://fyodortraining.testrail.io/'
user = 'fyodor.repollo@gurock.io'
password = ''


session = requests.Session()
session.auth = (user, password)


response = session.get(host + '/index.php?/api/v2/get_projects')


print(response.json())
print(session.cookies)
print(response.headers['Set-Cookie'])

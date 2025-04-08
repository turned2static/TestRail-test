import requests

# Set your TestRail host and API credentials
host = 'https://fyodortraining.testrail.io/'
user = 'fyodor.repollo@gurock.io'
password = 'Gurock6yhn7ujm'

# Authenticate to the TestRail API
session = requests.Session()
session.auth = (user, password)

# Send a GET request to the TestRail API to retrieve a list of projects
response = session.get(host + '/index.php?/api/v2/get_projects')

# Print the response
print(response.json())
print(session.cookies)
print(response.headers['Set-Cookie'])

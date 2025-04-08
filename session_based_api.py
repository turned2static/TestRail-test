from testrail import *
# Set up the TestRail client
client = APIClient('https://fyodortraining.testrail.io/')


# Prompt for the user and password
client.user = 'fyodor.repollo@gurock.io'
client.password = 'Gurock6yhn7ujm'

# Set up the credentials
credentials = {'email': client.user, 'password': client.password}

# Make the login request
response = requests.post(client, json=credentials)
print(response)

# Extract the session cookie from the response
session_cookie = response.cookies["TR_SESSION_ID"]
print(session_cookie)

# Use the session cookie for subsequent API requests
headers = {"Cookie": f"TR_SESSION_ID={session_cookie}"}
response = requests.get("https://fyodortraining.testrail.io/index.php?/api/v2/get_case/1", headers=headers)
print(response.json())

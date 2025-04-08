from testrail import *
from getpass import *

web_address = input('Enter your testrail address: ')
client = APIClient('https://' + web_address + '/')
#client = APIClient('https://fyodortraining.testrail.io/')
client.user = input('Enter your email address: ')
client.password = input('Enter your password: ')
#client.password = getpass('Password: ')

case = client.send_get('get_cases/37&suite_id=136')
#item_dict = json.loads(json_data)
#print len(item_dict['cases'][0]['id'])
print(case)
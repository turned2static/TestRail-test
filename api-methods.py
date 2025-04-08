from testrail import *
from getpass import *

web_address = input('Enter your testrail address: ')
client = APIClient('https://' + web_address + '/')
#client = APIClient('https://fyodortraining.testrail.io/')
client.user = input('Enter your email address: ')
client.password = input('Enter your password: ')
#client.password = getpass('Password: ')


#get request
#case = client.send_get('get_case/9757')
#print(case)

#post request
amount = int(input("Enter amount of test cases to add: "))
api_method = input("Enter API method: ")
id = int(input("Enter case/section/run ID: "))

value = 1
while value <= amount:
    result = client.send_post(
    api_method + "/" + str(id),
    { 'template_id': 2, 'title': 'This is an automated separated steps sample' + " " + str(value), 'custom_steps_separated': [{'content': 'Navigate to messaging app on mobile device',
                                                                                                                  'expected': 'Messaging app login page is displayed',
                                                                                                                  'additional_info': '',
                                                                                                                  'refs': ''},
                                                                                                                 {'content': 'Attempt to log in with false credentials',
                                                                                                                  'expected': 'Error message',
                                                                                                                  'additional_info': '',
                                                                                                                  'refs': ''},
                                                                                                                 {'content': 'Click forgot user link',
                                                                                                                  'expected': 'App opens forgot user flow',
                                                                                                                  'additional_info': '',
                                                                                                                  'refs': ''}]}
)

    print(result)
    value += 1    




'''
#attachment request
result = client.send_get('get_attachment/1', 'C:\\attachment.jpg')
result = client.send_post('add_attachment_to_result/1', 'C:\\screenshot.jpg')
'''
from testrail import *
 
client = APIClient('https://fyodortraining.testrail.io/')
client.user = 'fyodor.repollo@gurock.io'
client.password = 'Gurock6yhn7ujm'

#create test suite
project_id = int(input('Enter a project ID: '))
suite_name = input('Enter a Suite name: ')
payload = { 'name': suite_name, 'description': 'This is an automated Python test suite!' }
add_suite = client.send_post('add_suite/' + str(project_id), data=payload)

while True:
    print(add_suite)
    break

#get suite id
#create section
payload_section = { 'suite_id': add_suite['id'], 'name': 'Python test section!' }
add_section = client.send_post('add_section/' + str(project_id), data=payload_section)
while True:
    print(add_section)
    break

#add cases
num_cases = int(input('How many test cases would you like to add? '))
case_num = 0
payload_cases = { 'title': 'Python test case', 'name': 'Python test section!' }

while case_num <= num_cases:
    add_case = client.send_post('add_case/' + str(add_section['id']), data=payload_cases)
    print(add_case)
    case_num += 1
print('Adding test cases done!')

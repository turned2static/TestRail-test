# Import the required libraries
import random
from testrail import *


# Set up the TestRail client
client = APIClient('https://fyodortraining.testrail.io/')


# Prompt for the user and password
client.user = 'fyodor.repollo@gurock.io'
client.password = 'Gurock6yhn7ujm'


# Define the project where the test suite and test cases will be added
project_id = int(input('Enter a project ID: '))

# Create the test suite
suite_name = input('Enter a Suite name: ')
payload = { 'name': suite_name, 'description': 'This is an automated Python test suite!' }
try:
    add_suite = client.send_post('add_suite/' + str(project_id), data=payload)
    print("Test suite added successfully:", add_suite)
except APIError as err:
    print("Error adding test suite:", err)

# Define the number of sections to add to the test suite
num_sections = int(input('How many test sections would you like to add? '))

# Add the test sections to the test suite
sections = []
for i in range(num_sections):
    # Generate a random test section name
    random_name = "Test Section " + str(random.randint(1, 100))
    payload_section = { 'suite_id': add_suite['id'], 'name': random_name }
    try:
        add_section = client.send_post('add_section/' + str(project_id), data=payload_section)
        sections.append(add_section)
        print("Test section added successfully:", add_section)
    except APIError as err:
        print("Error adding test section:", err)

# Add the test cases
num_cases = int(input('How many test cases would you like to add? '))
results = []
# Move the case_num variable inside the while loop
case_num = 0
while case_num < num_cases:
    # Select a random section from the list of sections
    section = random.choice(sections)
    # Generate a random test case name
    random_name = "Test Case " + str(random.randint(1, 100))
    payload_cases = { 'title': random_name, 'name': random_name }
    try:
        add_case = client.send_post('add_case/' + str(section['id']), data=payload_cases)
        results.append(add_case)
        case_num += 1
        print("Test case added successfully:", add_case)
    except APIError as err:
        print("Error adding test case:", err)

print('Adding test cases done!')

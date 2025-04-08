import re

# Use a regular expression to search for lines that contain '[E]'
pattern = re.compile(r'\[E\]')

# Open the file in read-only mode
with open(r'C:\Users\3Monkeys\Downloads\log-2022-11-09.php', 'r') as phpfile:
    # Read each line in the file
    for line in phpfile:
        # Use the regular expression to search for '[E]' in the line
        if pattern.search(line):
            # If '[E]' is found, print the line
            print(line)
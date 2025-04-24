with open(r'C:\Users\Downloads\log-2022-11-09.php') as phpfile:
    # read each line of the file
    for x in phpfile.read().split('\n'):
        # if the word is found in the line
        # print it
        if x.find('[E]') != -1:
            print(x)
            

import webbrowser, sys, pyperclip

sys.argv # ['monster.py', 'Clinical' 'Assistant' ',' 'London']


# Convert ['monster.py', 'Clinical' 'Assistant' ',' 'London'] -> 'Clinical Assistant, London' (creates jobWhere)
jobWhere = ' '.join(sys.argv[1:])

# Split jobWhere
job, comma, location = jobWhere.partition(',')

webbrowser.open("https://www.monster.co.uk/jobs/search?q=" +job + "&where=" +location)

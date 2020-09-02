# navigate to desired directory in terminal and then call the program.
# example: user@machine~$omewhere/> python path/git.py
import os

# path = input('path: ')
repo = input('repository: ')

# this_file = os.getcwd()
# this_file += '\git.py'

os.system('git init')
os.system('git add -A')
os.system('git commit -m "add all files"')
os.system('git remote add github ' + repo)
os.system('git push -f github master')

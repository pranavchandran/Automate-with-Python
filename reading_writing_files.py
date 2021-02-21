# Reading and writing files

from pathlib import Path

print(Path('Spam', 'bacon', 'eggs'))
print(str(Path('Spam', 'bacon', 'eggs')))

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path(r'/home/ai', filename))

print(Path('spam')/'bacon'/'eggs')
print(Path('spam')/ Path('bacon')/'eggs')

homefolder = Path('root:/Users/pranavc')
subfolder = Path('pycoder')
print(homefolder/subfolder)

# current working dir
import os

print(Path.cwd())
# print(os.chdir('/home/pythonista/Automate_the_boring_stuff/lol'))
# print(Path.cwd())

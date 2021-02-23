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

# To find home dir
print('Home Dir: %s'%Path.home())

'''
Absolute vs. Relative Paths
There are two ways to specify a file path:
An absolute path, which always begins with the root folder
A relative path, which is relative to the program’s current working directory
'''

'''
Creating New Folders Using the os.makedirs() Function
'''
try:
    os.makedirs('test1')
except FileExistsError:
    print('Folder already exists')

'''
To make a directory from a Path object, call the mkdir() method. 
For example, this code will create a spam folder under the home 
folder on my computer:
'''

directory = "Pranav"
  
# Parent Directory path 
parent_dir = "/home/pythonista"
# mode 
mode = 0o666
# Path 
path = os.path.join(parent_dir, directory) 
# Create the directory 
# 'Pranav' in 
# '/home / User / ' 
# with mode 0o666 
try:
    os.mkdir(path, mode)
except FileExistsError:
    print('folder exists')

# Exception FileExistsError as e 
print("Directory '% s' created" % directory)  

# Handling Absolute and Relative Paths
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('kuttu/home').is_absolute())

Path('kuttu/one/path')
print(Path.cwd()/Path('kuttu/one/path'))

print(os.path.abspath('.'))
print(os.path.abspath('./Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs('/home/pythonista'))
print(os.path.isabs(os.path.abspath('.')))

p = Path('/home/pyhtonista.txt')
print(p.anchor)
print(p.parent)
print(p.parent)
print(p.suffix)

print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
# print(Path.cwd().parents[3])

calcfilepath = '/home/root/pranav.txt'
print(os.path.basename(calcfilepath))
print(os.path.dirname(calcfilepath))
print( os.path.dirname(calcfilepath), os.path.basename(calcfilepath))
print(calcfilepath.split(os.sep))

# Finding File Sizes and Folder Contents
print(os.path.getsize('/home/pythonista/Automate_the_boring_stuff'))
print(os.listdir('/home/pythonista/'))

'''
If I want to find the total size of all the files in this directory,
I can use os.path.getsize() and os.listdir() together.
'''
totalsize = 0
for filename in os.listdir('/home/pythonista/Automate_the_boring_stuff'):
    totalsize = totalsize + os.path.getsize(os.path.join\
        ('/home/pythonista/Automate_the_boring_stuff', filename))
    print(filename, '\t', totalsize)

'''
Modifying a List of Files Using Glob Patterns
'''
P = Path('/home/pythonista/Automate_the_boring_stuff/')
print(P.glob('*'))
print(list(P.glob('*')))
print(list(P.glob('*.txt')))
print(list(p.glob('project?.docx')))
print(list(P.glob('.py')))
print(list(p.glob('*.?x?')))

p = Path('/home/pythonista/Automate_the_boring_stuff/')
for txtfile in p.glob('*.txt'):
    print(txtfile)



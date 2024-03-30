#Write a Python program to copy the contents of a file to another file
import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:\Users\arsen\git_test\labs\lab 6\Files and directories manipulation/Copy.txt'
f2 = 'C:\Users\arsen\git_test\labs\lab 6\Files and directories manipulation/Copy2.txt'
copy(f1, f2)
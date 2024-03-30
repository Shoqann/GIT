#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = input("Insert your path: ")

if os.access(path, os.F_OK):
    print(os.listdir(path))
else: 
    print("The path does not exist")
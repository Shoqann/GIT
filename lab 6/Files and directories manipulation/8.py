#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists('ex.txt'):
    os.remove('ex.txt')
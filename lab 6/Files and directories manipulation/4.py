#Write a Python program to count the number of lines in a text file.
count = 0

with open("C:\\Users\\arsen\\git_test\\labs\\lab 6\\Files and directories manipulation\\Example.txt", "r") as txt:
    for i in txt:
        count += 1

print (count)
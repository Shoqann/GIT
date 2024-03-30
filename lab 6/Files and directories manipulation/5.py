#Write a Python program to write a list to a file.
with open("C:\\Users\\arsen\\git_test\\labs\\lab 6\\Files and directories manipulation\\Example.txt", "a") as txt:
    a = list(input("Write list: ").split())
    for i in a:
        txt.write(i + " ")
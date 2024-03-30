#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def polindrome(string):
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")

string = input("Insert your string: ")
polindrome(string)
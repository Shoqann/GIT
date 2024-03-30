#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def istrue (tuple):
    return all(tuple)

tuple_example = (True, True, True, True)

print(istrue(tuple_example))
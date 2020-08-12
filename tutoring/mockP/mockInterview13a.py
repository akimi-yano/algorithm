def ascii_printer(string):
    return "".join([str(ord(c)) for c in string])
print(ascii_printer("Hello my name is Pete"))


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return con_1(s) and con_2(s) and con_3(s) and con_4(s) and con_5(s)

def con_1(t):   # plate must have between 2 and 6 characters #
    return 2 <= len(t) <= 6

def con_2(t):   # plate must only have letters and numbers #
    return t.isalnum()

def con_3(t):   # plate stars with at least 2 letters #
    return t[0:2].isalpha()

def con_4(t):   # plate must end with numbers if they contain any number #
    if t.isalpha():
        return True
    elif t[0:2].isalpha() and t[2:].isdigit():
        return True
    elif t[0:3].isalpha() and t[3:].isdigit():
        return True
    elif t[0:4].isalpha() and t[4:].isdigit():
        return True
    elif t[0:5].isalpha() and t[5:].isdigit():
        return True
    else:
        return False

def con_5(t):   # plate numbers must not start with 0 #
    if t.isalpha():
        return True
    elif t[0:2].isalpha() and t[2] != '0':
        return True
    elif t[0:3].isalpha() and t[3] != '0':
        return True
    elif t[0:4].isalpha() and t[4] != '0':
        return True
    elif t[0:5].isalpha() and t[5] != '0':
        return True
    else:
        return False

if __name__ == "__main__":
    main()

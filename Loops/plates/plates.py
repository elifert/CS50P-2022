def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return first_two(s) and length(s) and ctrl_num(s) and check_zero(s) and no_punc(s)

def first_two(s):
    return s[:2].isalpha()

def length(s):
    return 2<=len(s)<=6

def ctrl_num(s):
    for count in range(len(s)-1):
        if s[count].isdigit() and s[count+1].isalpha():
            return False
    return True


def check_zero(s):
    numbers = [char for char in s if char.isdigit()]
    if numbers:
        return numbers[0]!="0"
    return True

def no_punc(s):
    punc = [" ", ",", ".", "!", "?", "-", ":", ";","_"]
    return all(char not in punc for char in s)

main()

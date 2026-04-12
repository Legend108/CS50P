import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if re.match(r"^[a-zA-Z]{2}([a-zA-Z]*|[a-zA-Z]*[1-9]{1}[0-9]*)$", s):
            return True
        else:
            return False
    else:
        return False


main()
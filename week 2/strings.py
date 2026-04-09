name = input("What's your name? ").title()
def main():
    # take the output from function and match with already coded inputs
    first = splitUsername()
    # print(splitUsername(name))
    match first:
        case "Daniel":
            print("Welcome", first)
        case False:
            print("Maximum number of names crossed")
        case _:
            print("Could not find user", first)

# Split usernames and check length for name, middle name and surname
# return only the first name after handling all three cases

def splitUsername(username="NoArguments"):
    count = len(username.split(" "))
    # Alternate way using if elif statements
    # if count == 1:
    #     return name
    # elif count == 2:
    #     first, last = name.split(" ")
    #     return first
    # elif count == 3:
    #     first, middle, last = name.split(" ")
    #     return first
    # else:
    #     return False
    match count:
        case 1:
            return username
        case 2:
            first, last=username.split(" ")
            return first
        case 3:
            first, middle, last = username.split(" ")
            return first
        case False:
            return
        case _:
            return False

main()

#CS50P 2022 Loop

names = []

# Open the file as readonly since default is "r"
with open("file.txt") as file:
    for name in file.readlines():
        names.append(name)
# read all the names line wise and add into a temporary list
for name in sorted(names, reverse=True): # reverse is false default
    print("Hello", name.rstrip())
# sort the list using sorted, alphabetically (reverse)
# Strip the whitespace at the end and print with Hello
with open("file.txt", "r") as file:
    lines = file.readlines()
# returns an array of lines separated
for line in lines:
    print(line.rstrip())    # Remove whitespace from end of the string
import re


username = input("What's your username? ").strip()

if matches := re.search("^([a-zA-Z]+), *([a-zA-Z]+)$", username): # Walrus operator, assigns the value AND asks a true/false question
    print("Hello", matches.group(1).title(), matches.group(2).title())
else:
    print(username)
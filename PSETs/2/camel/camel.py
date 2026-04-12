import re

camel = input("Camel case: ")
snake = ""
if re.match(r"^[a-z]+([A-Z][a-z]*)+$", camel):
    for char in camel:
        snake += char
        if char.isupper():
            snake = snake.replace(char, f"_{char.lower()}")
    print("Snake case: " + snake)
else:
    print("That is NOT snake case")


# can also use re.sub, reduces the code to like one line
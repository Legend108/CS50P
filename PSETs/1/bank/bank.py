import re

greet = input("Greeting: ").strip().lower()
if re.search("^hello.*$", greet):
    print("$0")
elif re.search("^h.*$", greet):
    print("$20")
else:
    print("$100")
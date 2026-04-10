import re

email = input("Enter your email: ")
# basic as hell
if re.search(r"^\w+\.?\w+@\w+\.?\w+\.(edu|com|net)", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Can use re.fullsearch(same arguments) to prevent using the ^ and $ to check for edge cases
# re.search(pattern, string, flags=0)
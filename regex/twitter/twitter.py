import re

url = input("Provide URL: ")

#https://twitter.com/davidjmalan

if find_user := re.search(r"^(?:https?(?::?/?/?)?(?:www\.|mobile\.)?)?(?:twitter\.com|x\.com)/(\w{1,15}).*$", url, re.IGNORECASE):
    print(find_user.group(1))
# can use re.sub to replace using a pattern but not that useful YET
else:
    print("Invalid link")
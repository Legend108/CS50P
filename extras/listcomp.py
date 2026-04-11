"""gryffindors = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindor = [gryffindor["name"].lower() for gryffindor in gryffindors if gryffindor["house"] == "Gryffindor"]

print(*gryffindor)
"""
# above is an alternate way of doing this also called a list comprehension
gryffindors = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ian", "house": "Gryffindor"}
]

def is_gryffindor(guy):
    if guy["house"] == "Gryffindor":
        return True

gryffindor = filter(is_gryffindor, gryffindors)
# Pass in a function on the basis of which its gonna filter
for obj in sorted(gryffindor, key=lambda s: s["name"]):
    print(obj["name"], end=" ")
# Sort alphabetically on the basis of the name key
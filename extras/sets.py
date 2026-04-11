houses = set() # Just like a set in math, no repetitive letters

letters = ["a", "a", "b", "c"]
for letter in letters:
    houses.add(letter) # add for set, append for list

print(sorted(houses, reverse=True))    
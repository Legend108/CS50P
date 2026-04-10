names = []

for _ in range(3):
    name = input("Whats your name? ")
    names.append(name)
# This is temporary, in the program memory, it forgets after restarting

for name in sorted(names):
    print("Hello", name)
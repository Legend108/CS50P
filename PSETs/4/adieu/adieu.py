import inflect
i = inflect.engine()
names: list = []

def main():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError: # Ctrl+Z and Enter triggers an EOFError, Ctrl+d for mac or linux
            print("Adieu, adieu to,", i.join(names))
            break

if __name__ == "__main__":
    main()
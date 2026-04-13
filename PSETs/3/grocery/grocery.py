def main():
    grocery_counts = {}
    while True:
        try:
            inp = input()
            if not inp:
                continue
            if inp in grocery_counts:
                grocery_counts[inp] += 1
            else:
                grocery_counts[inp] = 1
        except EOFError:
            for keys in sorted(grocery_counts.keys()):
                print(f"{grocery_counts[keys]} {keys}")
            break
if __name__ == "__main__":
    main()
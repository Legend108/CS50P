while True:
    try:
        mass = int(input("Enter mass: "))
        print(mass*300000000*300000000)
        break
    except ValueError:
        print("Enter a valid number")
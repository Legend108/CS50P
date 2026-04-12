amount = 50

while True:
    try:
        if amount > 0:
            print("Amount owed:", amount)
            x = int(input("Insert coin: ").strip())
            if x in [25,10,5]:
                amount -= x
        elif amount == 0:
            print("Change owed:", 0)
            break
        else:
            print("Change owed:", -amount)
            break
    except ValueError:
        print("Invalid integer")
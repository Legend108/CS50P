items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Choose an item: ").strip().lower().title()
        if items[item]:
            total += items[item]
            print("Total:", total)
        else:
            continue
    except EOFError:
        print(f"Your price is ${total}")
        break
    except KeyError:
        continue
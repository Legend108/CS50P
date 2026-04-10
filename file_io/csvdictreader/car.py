import csv

while True:
    try: 
        min_hp = int(input("Minimum horsepower: "))
        break
    except ValueError:
        print("Provide a valid number")

filtered_list = []

with open("car.csv") as file:
    reader = csv.DictReader(file)
    # with reader it returns an array with strings that were separated by the commas
    # dict reader returns an object with the column names
    for row in reader:
        try:
            if int(row["hp"]) >= min_hp:
                filtered_list.append({"owner": row["owner"], "car": row["car"], "hp": row["hp"]})
        except ValueError:
            print("Invalid CSV file. (HP is not valid)")

# Get the different lists, and then use the temp lambda function to sort only on the basis of the owner name
for user in sorted(filtered_list, key=lambda user: user["owner"]):
    print(f"{user['owner']} drives a {user['car']} ({user['hp']} HP)")
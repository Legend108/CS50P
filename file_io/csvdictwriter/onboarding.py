import csv
import os

name = input("Username: ")
email = input("Email: ")

while True:
    plan = input("Plan(Pro(P)/Basic(B)): ").strip().upper() # upper does the whole string, capitalize does only the first letter
    # strip removes all whitespaces, rstrip does only the end and lstrip does the start
    match plan:
        case "P" | "B" | "PRO" | "BASIC":
            if plan in ["P", "PRO"]:
                plan = "PRO"
            elif plan in ["B", "BASIC"]:
                plan = "BASIC"
            break
        case _:
            print("Invalid option")

check_file = os.path.isfile("credentials.csv")
# check for existence of file for creation of headers
with open("credentials.csv", "a") as file:
    header_structure = ["name", "email", "plan"]
    writer = csv.DictWriter(file, fieldnames=header_structure)

    if not check_file:
        writer.writeheader()

    writer.writerow({"name": name, "email": email, "plan": plan})
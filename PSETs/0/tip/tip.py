import re
def main():
    dollars: float = dollars_to_float(input("How much was the meal? "))
    percent: float = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d:str) -> float:
    if re.match(r"^\$[0-9]+\.[0-9]{2}$", d):
        return float(d.replace("$", ""))
    else:
        print("Invalid syntax")
        raise ValueError("Wrong amount format")


def percent_to_float(p) -> float:
    if re.match(r"^[0-9]{1,2}%$", p):
        return float(p.replace("%", ""))/100
    else:
        print("Invalid syntax")
        raise ValueError("Wrong amount format")


main()